---
title: "Pruning"
slug: "global-synchronizer-production-operations-pruning"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/pruning.md"
source_title: "Pruning"
tags:
  - global-synchronizer
  - production-operations
  - pruning
---

# Pruning

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Pruning

> Sequencer and CometBFT pruning configuration for Global Synchronizer nodes

This page covers Canton-side pruning for participant nodes and automatic pruning configuration.

For Super Validator pruning of the sequencer and CometBFT layers, see [SV Pruning](/global-synchronizer/production-operations/sv-pruning).

## Participant node pruning

Pruning helps bound the size of the database storage. Participant Node pruning refers to the selective removal of archived contracts and old transactions. Select one of two options, choosing between ease-of-use and control:

1. Automatic pruning instructs the Participant Node to perform pruning according to a regular schedule and retention period.
2. Manual pruning provides explicit control over the ledger offset to prune up to. In addition, manual pruning allows integration of pruning with operational procedures such as database backups and defragmentation.

As a prerequisite to pruning, put in place backups and ensure that a backup is taken each time you prune the Participant Node. Refer to the backup and restore for specifics.

### Enable automatic pruning

Enable automatic pruning by specifying a pruning schedule consisting of the following:

* A cron expression that designates regular pruning begin times.
* A maximum duration specifying pruning end times relative to the begin times of the cron expression.
* A retention period to specify how far to prune relative to the current time.
* An optional indication of whether to prune internal stores only, or by default, to prune Ledger API visible archived contracts and updates as well.

For example, to run pruning every Saturday starting at 8 AM until 4 PM (both in UTC):

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant.pruning.set_participant_schedule(
  cron = "0 0 8 ? * SAT",
  maxDuration = 8.hours,
  retention = 90.days,
  pruneInternallyOnly = false,
)
```

On Participant Nodes configured for high availability that share a common database, the methods modifying the pruning schedule have to be invoked on the active Participant Node replica.

Refer to automatic pruning for a reference to the other available automatic pruning methods.

### Perform manual pruning

Manually pruning Participant Nodes allows composing pruning with database maintenance operations, but requires identifying an explicit ledger offset up to which the ledger should be pruned.

1. Identify the numeric ledger offset up to which to prune the ledger by specifying the time up to which to prune:

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   val offsetToPruneUpTo = participant.pruning.find_safe_offset(timeToPruneUpTo.toInstant)
   ```

   The `find_safe_offset` method returns `None` if no offset corresponds to the specified time.

2. Invoke manual pruning on the Participant Node.

   In almost all cases, choose the comprehensive `prune` method that frees up the most storage, but also reduces the portion of the ledger visible via the Ledger API.

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   // The prune() method prunes more comprehensively and should be used in most cases.
   participant.pruning.prune(offsetToPruneUpTo)
   ```

   In some cases, you might elect to use the `prune_internally` method in addition to the `prune` method. Typically, you invoke the `prune_internally` method after the `prune` method and with a larger offset. For example, this way you can retain three months of the Ledger API history, but prune the internal stores up to one month.

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   // The prune() method prunes more comprehensively and should be used in most cases.
   participant.pruning.prune_internally(offsetToPruneUpTo, None)
   ```

   On Participant Nodes that are configured for high availability and share a common database, the pruning methods have to be invoked on the active Participant Node replica.

The `prune` and `prune_internally` methods might appear to be hanging unless the ledger offset is iteratively increased in sufficiently small increments for piecemeal pruning via multiple methods calls. In addition, these manual methods have no built-in mechanism to resume on another node after a high-availability failover.

### Defragment the database

Defragment the database after pruning. Pruning deletes data from the database, freeing up space, but it does not resize tables. Refer to the PostgreSQL documentation on `VACUUM` and `VACUUM FULL` for more information on how to optimally reclaim the space freed up by pruning.

### Monitor pruning progress

Monitor the pruning state to determine that the pruning schedule allows pruning to keep up with ledger growth, and that automatic pruning is not stuck for one of the reasons described below as pruning limitations.

Monitor the `daml_pruning_max_event_age` metric describing the age of the "oldest, un-pruned" event (in hours). The `max-event-age` metrics should not exceed the value of the pruning schedule `retention` plus the length of the interval. For example, if your schedule specifies a retention of 30 days and a cron that calls for weekly pruning, `max-event-age` must remain below 37 days. If for any node the `max-event-age` metric exceeds this upper limit, consider allocating more time for pruning by reducing the interval between pruning windows, or by increasing the `maximum duration` pruning schedule setting.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/reference/automatic_pruning.rst" hash="6e2b1915" */}

### Automatic pruning reference

The following functions are available to set, modify, and read the pruning schedule:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Set a pruning schedule with a duration and a retention period.
pruning.set_schedule("0 0 8 ? * SAT", 8.hours, 90.days)

// Retrieve the current pruning schedule returning `None` if no schedule is set.
val pruningSchedule = pruning.get_schedule()

// Set individual fields to modify the existing pruning schedule.
pruning.set_cron("0 /5 * * * ?")
pruning.set_retention(30.days)
pruning.set_max_duration(2.hours)

// Clear the pruning schedule disabling automatic pruning on a specific node.
pruning.clear_schedule()
```

Refer to the cron specification to customize the pruning schedule. Here are a few examples:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Prune every evening at 8pm GMT for two hours
set_schedule("0 0 20 * * ?", 2.hours, retention)

// Prune every 5 minutes for one minute
set_schedule("0 /5 * * * ?", 1.minute, retention)

// Prune for one specific day
set_schedule("0 0 0 31 12 ? 2025", 1.day, retention)
```

For the maximum duration to specify a reliable pruning window end time, the leading fields of the cron expression must not be wildcards (`\*`), as illustrated in the preceding examples. If the hour field is fixed, the fields for the minute and the second must be fixed too.

#### Schedule format

Cron expressions are formatted as seven whitespace-separated fields:

| Field            | Type and valid values\*                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| seconds          | number from `0` to `59`                                                                                             |
| minutes          | number from `0` to `59`                                                                                             |
| hours            | number from `0` to `23`                                                                                             |
| day of the month | number from `1` to `31`                                                                                             |
| month            | number from `0` to `11` (`0` = January) **or** the first three letters of the month name (`JAN`, `FEB`, `MAR`, etc) |
| day of the week  | number from `1` to `7` (`1` = Sunday) **or** the first three letters of the day name (`SUN`, `MON`, `TUE`, etc)     |
| year (optional)  | number from `1900` to `2099`                                                                                        |

*\*Ranges specified with "from .. to .." are inclusive of both endpoints.*

Note that, although a day-of-the-month value might be valid according to the preceding definition, it might not correspond to an actual date in certain months (such as the thirty-first of November). If you schedule pruning for the thirty-first of the month, every month with fewer than 31 days is skipped.

#### Advanced schedule formatting

* You can construct **lists and ranges** of values. For example, the day of the week could be a range like `MON-FRI` to refer to the days Monday through Friday, or `TUE,FRI` to refer to Tuesday and Friday exclusively. Or you could use a mix of both, for example, `MON,WED-FRI`, meaning "Monday, and also Wednesday through Friday."
* Use the **asterisk** (`*`) as a wildcard that means "all possible values."
* Use the **question mark** (`?`) as a wildcard that means "any value" in the day-of-the-month and day-of-the-week fields. For example, to specify "every Monday at noon," use the `?` character to indicate that any day of the month is valid: `0 0 12 ? * MON`
* To apply **increments** to numeric values, use the slash character (`/`). For example, a value of `1/2` in the hours field means "every two hours starting from 1 AM" (1 AM, 3 AM, 5 AM, etc).

Here are some examples of valid schedules:

* `0 30 * * * *` Every hour at half past
* `0 5/15 12,18-20 * * *` Every fifteen minutes, starting from five past, at noon and from 6 to 8 PM
* `0 5/15 12,18-20 ? * MON,THU` Same as above, but only on Mondays and Thursdays
* `0 0 22 1 * ?` Every first day of the month at 10 PM

For more information about cron expressions, see the [Apache Log4j API documentation](https://logging.apache.org/log4j/2.x/javadoc/log4j-core/org/apache/logging/log4j/core/util/CronExpression.html).

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.

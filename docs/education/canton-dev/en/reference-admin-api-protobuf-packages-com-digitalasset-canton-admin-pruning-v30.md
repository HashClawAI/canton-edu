---
title: "com.digitalasset.canton.admin.pruning.v30"
slug: "reference-admin-api-protobuf-packages-com-digitalasset-canton-admin-pruning-v30"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/packages/com-digitalasset-canton-admin-pruning-v30.md"
source_title: "com.digitalasset.canton.admin.pruning.v30"
tags:
  - reference
  - admin-api
  - protobuf
  - packages
---

# com.digitalasset.canton.admin.pruning.v30

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# com.digitalasset.canton.admin.pruning.v30

> Package-level overview for com.digitalasset.canton.admin.pruning.v30.

<p class="x2mdx-ref-back"><a href="/docs/canton/reference-admin-api-protobuf-index">Back to overview</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf Package</p>

  <h1 class="x2mdx-ref-title">com.digitalasset.canton.admin.pruning.v30</h1>

  <p class="x2mdx-ref-summary">0 services, 0 endpoints, 28 messages</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>Files</dt>
      <dd>1</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Services</dt>
      <dd>0</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Endpoints</dt>
      <dd>0</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Messages</dt>
      <dd>28</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Enums</dt>
      <dd>0</dd>
    </div>
  </dl>
</div>

## Source Files

<div class="x2mdx-ref-card-grid">
  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/pruning/v30/pruning.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Current source file in the latest published descriptor snapshot.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Services</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Messages</dt>
        <dd>28</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Enums</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Source</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/pruning/v30/pruning.proto">community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/pruning/v30/pruning.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## Type Inventory

These are the package-level message and enum shapes in the publish-version snapshot.

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-clearschedulerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.ClearScheduleRequest</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-clearscheduleresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.ClearScheduleResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-findpruningtimestamprequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.FindPruningTimestampRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">index</code>
        <span class="x2mdx-ref-type-badge">int32</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-findpruningtimestampresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.FindPruningTimestampResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">timestamp</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-getnowaitcommitmentsfromrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.GetNoWaitCommitmentsFromRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_ids</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">participant\_uids</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-getnowaitcommitmentsfromresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.GetNoWaitCommitmentsFromResponse</h3>

    <p class="x2mdx-ref-schema-summary">2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">ignored\_participants</code>
        <span class="x2mdx-ref-type-badge">repeated WaitCommitmentsSetup</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">not\_ignored\_participants</code>
        <span class="x2mdx-ref-type-badge">repeated WaitCommitmentsSetup</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-waitcommitmentssetup">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.WaitCommitmentsSetup</h3>

    <p class="x2mdx-ref-schema-summary">2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">counter\_participant\_uid</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizers</code>
        <span class="x2mdx-ref-type-badge">Synchronizers</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-synchronizers">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.Synchronizers</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_ids</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-getparticipantschedulerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.GetParticipantScheduleRequest</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-getparticipantscheduleresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.GetParticipantScheduleResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">schedule</code>
        <span class="x2mdx-ref-type-badge">ParticipantPruningSchedule</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-participantpruningschedule">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.ParticipantPruningSchedule</h3>

    <p class="x2mdx-ref-schema-summary">2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">schedule</code>
        <span class="x2mdx-ref-type-badge">PruningSchedule</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">prune\_internally\_only</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-pruningschedule">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.PruningSchedule</h3>

    <p class="x2mdx-ref-schema-summary">3 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">cron</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">max\_duration</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">retention</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-getschedulerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.GetScheduleRequest</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-getscheduleresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.GetScheduleResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">schedule</code>
        <span class="x2mdx-ref-type-badge">PruningSchedule</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-resetnowaitcommitmentsfromrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.ResetNoWaitCommitmentsFromRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">counter\_participant\_ids</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_ids</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-resetnowaitcommitmentsfromresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.ResetNoWaitCommitmentsFromResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setcronrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetCronRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">cron</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setcronresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetCronResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setmaxdurationrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetMaxDurationRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">max\_duration</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setmaxdurationresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetMaxDurationResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setnowaitcommitmentsfromrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetNoWaitCommitmentsFromRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">counter\_participant\_ids</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_ids</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setnowaitcommitmentsfromresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetNoWaitCommitmentsFromResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setparticipantschedulerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetParticipantScheduleRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">schedule</code>
        <span class="x2mdx-ref-type-badge">ParticipantPruningSchedule</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setparticipantscheduleresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetParticipantScheduleResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setretentionrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetRetentionRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">retention</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setretentionresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetRetentionResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setschedulerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetScheduleRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">schedule</code>
        <span class="x2mdx-ref-type-badge">PruningSchedule</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setscheduleresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetScheduleResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.

/**
 * Matrix-style character rain (global site). Targets #mx-rain-canvas.
 * Skipped when prefers-reduced-motion: reduce.
 */
(function () {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var canvas = document.getElementById('mx-rain-canvas');
  if (!canvas || !canvas.getContext) return;
  var ctx = canvas.getContext('2d');
  var chars =
    'ｦｧｨｩｪｫｬｭｮｯｱｲｳｴｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃ0123456789ABCDEFﾊﾋﾌﾍﾎﾏ';
  var fontSize = 15;
  var w = 0;
  var h = 0;
  var columns = 0;
  var drops = [];

  function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
    columns = Math.ceil(w / fontSize);
    while (drops.length < columns) drops.push(1);
    drops.length = columns;
  }

  window.addEventListener('resize', resize);
  resize();

  function tick() {
    ctx.fillStyle = 'rgba(0, 8, 2, 0.11)';
    ctx.fillRect(0, 0, w, h);
    ctx.font = fontSize + 'px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
    for (var i = 0; i < columns; i++) {
      var ch = chars[Math.floor(Math.random() * chars.length)];
      var x = i * fontSize;
      var y = drops[i] * fontSize;
      var flick = Math.random() > 0.96;
      ctx.fillStyle = flick ? '#ccffee' : '#00cc55';
      ctx.fillText(ch, x, y);
      if (y > h && Math.random() > 0.978) drops[i] = 0;
      drops[i]++;
    }
  }

  setInterval(tick, 48);
})();

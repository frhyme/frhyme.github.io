---
title: markdown에 html 소스를 넣으려고 합니다. 
category: others
tags: markdown html 
---

## 마크다운에 html 소스를 넣으려고 합니다. 

- 별거 아닙니다. 마크다운에 html 소스를 그대로 넣어도 문제없이 되는지 궁금합니다. 
- 하고보니 그냥 넣어도 잘만 되네요 하하핫.

```html
<h2>This is h2!!</h2>

<p> This is paragraph</p>
<link href="http://cdn.pydata.org/bokeh/dev/bokeh-0.13.0.min.css" rel="stylesheet" type="text/css">
<script src="http://cdn.pydata.org/bokeh/dev/bokeh-0.13.0.min.js"></script>

<script>
</script>
<div></div>
```

<h2>This is h2!!</h2>

<p> This is paragraph</p>

<link
    href="http://cdn.pydata.org/bokeh/dev/bokeh-0.13.0.min.css"
    rel="stylesheet" type="text/css"
>
<script 
    src="http://cdn.pydata.org/bokeh/dev/bokeh-0.13.0.min.js"
></script>

<script type="text/javascript">
  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {
            
          var docs_json = '{"8a107733-ae1b-4278-aff2-fa34e23850af":{"roots":{"references":[{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":15},"x":{"field":"x"},"y":{"field":"y"}},"id":"1509","type":"Circle"},{"attributes":{},"id":"1478","type":"LinearScale"},{"attributes":{"callback":null,"data":{"x":[1,2,3,4,5],"y":[6,7,2,4,5]},"selected":{"id":"1519","type":"Selection"},"selection_policy":{"id":"1518","type":"UnionRenderers"}},"id":"1507","type":"ColumnDataSource"},{"attributes":{},"id":"1518","type":"UnionRenderers"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"1500","type":"BoxAnnotation"},{"attributes":{},"id":"1480","type":"LinearScale"},{"attributes":{"fill_alpha":{"value":0.5},"fill_color":{"value":"orange"},"line_color":{"value":"navy"},"size":{"units":"screen","value":15},"x":{"field":"x"},"y":{"field":"y"}},"id":"1508","type":"Circle"},{"attributes":{},"id":"1519","type":"Selection"},{"attributes":{"callback":null},"id":"1474","type":"DataRange1d"},{"attributes":{"data_source":{"id":"1507","type":"ColumnDataSource"},"glyph":{"id":"1508","type":"Circle"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1509","type":"Circle"},"selection_glyph":null,"view":{"id":"1511","type":"CDSView"}},"id":"1510","type":"GlyphRenderer"},{"attributes":{"formatter":{"id":"1516","type":"BasicTickFormatter"},"plot":{"id":"1473","subtype":"Figure","type":"Plot"},"ticker":{"id":"1483","type":"BasicTicker"}},"id":"1482","type":"LinearAxis"},{"attributes":{"source":{"id":"1507","type":"ColumnDataSource"}},"id":"1511","type":"CDSView"},{"attributes":{},"id":"1492","type":"PanTool"},{"attributes":{"callback":null},"id":"1476","type":"DataRange1d"},{"attributes":{},"id":"1483","type":"BasicTicker"},{"attributes":{},"id":"1493","type":"WheelZoomTool"},{"attributes":{"plot":{"id":"1473","subtype":"Figure","type":"Plot"},"ticker":{"id":"1483","type":"BasicTicker"}},"id":"1486","type":"Grid"},{"attributes":{"overlay":{"id":"1500","type":"BoxAnnotation"}},"id":"1494","type":"BoxZoomTool"},{"attributes":{"formatter":{"id":"1514","type":"BasicTickFormatter"},"plot":{"id":"1473","subtype":"Figure","type":"Plot"},"ticker":{"id":"1488","type":"BasicTicker"}},"id":"1487","type":"LinearAxis"},{"attributes":{},"id":"1495","type":"SaveTool"},{"attributes":{},"id":"1516","type":"BasicTickFormatter"},{"attributes":{"plot":null,"text":""},"id":"1512","type":"Title"},{"attributes":{},"id":"1496","type":"ResetTool"},{"attributes":{},"id":"1488","type":"BasicTicker"},{"attributes":{},"id":"1514","type":"BasicTickFormatter"},{"attributes":{},"id":"1497","type":"HelpTool"},{"attributes":{"dimension":1,"plot":{"id":"1473","subtype":"Figure","type":"Plot"},"ticker":{"id":"1488","type":"BasicTicker"}},"id":"1491","type":"Grid"},{"attributes":{"below":[{"id":"1482","type":"LinearAxis"}],"left":[{"id":"1487","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"1482","type":"LinearAxis"},{"id":"1486","type":"Grid"},{"id":"1487","type":"LinearAxis"},{"id":"1491","type":"Grid"},{"id":"1500","type":"BoxAnnotation"},{"id":"1510","type":"GlyphRenderer"}],"title":{"id":"1512","type":"Title"},"toolbar":{"id":"1498","type":"Toolbar"},"x_range":{"id":"1474","type":"DataRange1d"},"x_scale":{"id":"1478","type":"LinearScale"},"y_range":{"id":"1476","type":"DataRange1d"},"y_scale":{"id":"1480","type":"LinearScale"}},"id":"1473","subtype":"Figure","type":"Plot"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1492","type":"PanTool"},{"id":"1493","type":"WheelZoomTool"},{"id":"1494","type":"BoxZoomTool"},{"id":"1495","type":"SaveTool"},{"id":"1496","type":"ResetTool"},{"id":"1497","type":"HelpTool"}]},"id":"1498","type":"Toolbar"}],"root_ids":["1473"]},"title":"Bokeh Application","version":"1.0.2"}}';
          var render_items = [{"docid":"8a107733-ae1b-4278-aff2-fa34e23850af","roots":{"1473":"5c624313-e483-4b36-8597-5dbe5575c64a"}}];
          root.Bokeh.embed.embed_items(docs_json, render_items);
        
          }
          if (root.Bokeh !== undefined) {
            embed_document(root);
          } else {
            var attempts = 0;
            var timer = setInterval(function(root) {
              if (root.Bokeh !== undefined) {
                embed_document(root);
                clearInterval(timer);
              }
              attempts++;
              if (attempts > 100) {
                console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                clearInterval(timer);
              }
            }, 10, root)
          }
        })(window);
      });
    };
    if (document.readyState != "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  })();
</script>
<div class="bk-root" id="2b7594c5-076f-4dd7-a00e-9765a6591b58"></div>
---
title: markdown에 html 소스를 넣으려고 합니다. 
category: others
tags: markdown html script
---

## 마크다운에 html 소스를 넣으려고 합니다. 

- 별거 아닙니다. 마크다운에 html 소스를 그대로 넣어도 문제없이 되는지 궁금합니다. 
- 기본적인 html 태그들은 잘 됩니다. 현재 작성하고 있는 내용이 마크다운이 아니라, html파일이라고 생각하고 진행해도 문제없이 됩니다. 
- 하고보니 그냥 넣어도 잘만 되네요 하하핫.

```html
<h2>This is h2!!</h2>

<p> This is paragraph</p>

<!--required library-->
<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-1.0.4.min.css" type="text/css" />
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-1.0.4.min.js"></script>
<script type="text/javascript">
    Bokeh.set_log_level("info");
</script>

<!--figure-->
 <div class="bk-root" id="409a6f0d-0035-44f0-aeff-7d5b10db7214" data-root-id="1001"></div>
<script type="application/json" id="1112">
    {"bd9b9da1-a044-454d-a80d-b81d6bdf734e":{"roots":{"references":[{"attributes":{"callback":null},"id":"1004","type":"DataRange1d"},{"attributes":{"overlay":{"id":"1028","type":"BoxAnnotation"}},"id":"1022","type":"BoxZoomTool"},{"attributes":{"plot":{"id":"1001","subtype":"Figure","type":"Plot"},"ticker":{"id":"1011","type":"BasicTicker"}},"id":"1014","type":"Grid"},{"attributes":{},"id":"1023","type":"SaveTool"},{"attributes":{"formatter":{"id":"1042","type":"BasicTickFormatter"},"plot":{"id":"1001","subtype":"Figure","type":"Plot"},"ticker":{"id":"1016","type":"BasicTicker"}},"id":"1015","type":"LinearAxis"},{"attributes":{"plot":null,"text":""},"id":"1040","type":"Title"},{"attributes":{},"id":"1024","type":"ResetTool"},{"attributes":{},"id":"1016","type":"BasicTicker"},{"attributes":{},"id":"1042","type":"BasicTickFormatter"},{"attributes":{},"id":"1025","type":"HelpTool"},{"attributes":{"dimension":1,"plot":{"id":"1001","subtype":"Figure","type":"Plot"},"ticker":{"id":"1016","type":"BasicTicker"}},"id":"1019","type":"Grid"},{"attributes":{"below":[{"id":"1010","type":"LinearAxis"}],"left":[{"id":"1015","type":"LinearAxis"}],"renderers":[{"id":"1010","type":"LinearAxis"},{"id":"1014","type":"Grid"},{"id":"1015","type":"LinearAxis"},{"id":"1019","type":"Grid"},{"id":"1028","type":"BoxAnnotation"},{"id":"1038","type":"GlyphRenderer"}],"title":{"id":"1040","type":"Title"},"toolbar":{"id":"1026","type":"Toolbar"},"x_range":{"id":"1002","type":"DataRange1d"},"x_scale":{"id":"1006","type":"LinearScale"},"y_range":{"id":"1004","type":"DataRange1d"},"y_scale":{"id":"1008","type":"LinearScale"}},"id":"1001","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"1044","type":"BasicTickFormatter"},{"attributes":{"data_source":{"id":"1035","type":"ColumnDataSource"},"glyph":{"id":"1036","type":"Circle"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1037","type":"Circle"},"selection_glyph":null,"view":{"id":"1039","type":"CDSView"}},"id":"1038","type":"GlyphRenderer"},{"attributes":{"callback":null,"data":{"x":[1,2,5,6,7],"y":[3,4,7,8,9]},"selected":{"id":"1047","type":"Selection"},"selection_policy":{"id":"1048","type":"UnionRenderers"}},"id":"1035","type":"ColumnDataSource"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1020","type":"PanTool"},{"id":"1021","type":"WheelZoomTool"},{"id":"1022","type":"BoxZoomTool"},{"id":"1023","type":"SaveTool"},{"id":"1024","type":"ResetTool"},{"id":"1025","type":"HelpTool"}]},"id":"1026","type":"Toolbar"},{"attributes":{},"id":"1006","type":"LinearScale"},{"attributes":{},"id":"1047","type":"Selection"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"1028","type":"BoxAnnotation"},{"attributes":{"callback":null},"id":"1002","type":"DataRange1d"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"1037","type":"Circle"},{"attributes":{},"id":"1008","type":"LinearScale"},{"attributes":{},"id":"1048","type":"UnionRenderers"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"1036","type":"Circle"},{"attributes":{},"id":"1020","type":"PanTool"},{"attributes":{"formatter":{"id":"1044","type":"BasicTickFormatter"},"plot":{"id":"1001","subtype":"Figure","type":"Plot"},"ticker":{"id":"1011","type":"BasicTicker"}},"id":"1010","type":"LinearAxis"},{"attributes":{"source":{"id":"1035","type":"ColumnDataSource"}},"id":"1039","type":"CDSView"},{"attributes":{},"id":"1021","type":"WheelZoomTool"},{"attributes":{},"id":"1011","type":"BasicTicker"}],"root_ids":["1001"]},"title":"Bokeh Application","version":"1.0.4"}}
</script>
<script type="text/javascript">
    (function() {
    var fn = function() {
        Bokeh.safely(function() {
        (function(root) {
            function embed_document(root) {
            
            var docs_json = document.getElementById('1112').textContent;
            var render_items = [{"docid":"bd9b9da1-a044-454d-a80d-b81d6bdf734e","roots":{"1001":"409a6f0d-0035-44f0-aeff-7d5b10db7214"}}];
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


```

<h2>This is h2!!</h2>

<p> This is paragraph</p>

<!--required library-->
<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-1.0.4.min.css" type="text/css" />
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-1.0.4.min.js"></script>
<script type="text/javascript">
    Bokeh.set_log_level("info");
</script>

<!--figure-->
 <div class="bk-root" id="409a6f0d-0035-44f0-aeff-7d5b10db7214" data-root-id="1001"></div>
<script type="application/json" id="1112">
    {"bd9b9da1-a044-454d-a80d-b81d6bdf734e":{"roots":{"references":[{"attributes":{"callback":null},"id":"1004","type":"DataRange1d"},{"attributes":{"overlay":{"id":"1028","type":"BoxAnnotation"}},"id":"1022","type":"BoxZoomTool"},{"attributes":{"plot":{"id":"1001","subtype":"Figure","type":"Plot"},"ticker":{"id":"1011","type":"BasicTicker"}},"id":"1014","type":"Grid"},{"attributes":{},"id":"1023","type":"SaveTool"},{"attributes":{"formatter":{"id":"1042","type":"BasicTickFormatter"},"plot":{"id":"1001","subtype":"Figure","type":"Plot"},"ticker":{"id":"1016","type":"BasicTicker"}},"id":"1015","type":"LinearAxis"},{"attributes":{"plot":null,"text":""},"id":"1040","type":"Title"},{"attributes":{},"id":"1024","type":"ResetTool"},{"attributes":{},"id":"1016","type":"BasicTicker"},{"attributes":{},"id":"1042","type":"BasicTickFormatter"},{"attributes":{},"id":"1025","type":"HelpTool"},{"attributes":{"dimension":1,"plot":{"id":"1001","subtype":"Figure","type":"Plot"},"ticker":{"id":"1016","type":"BasicTicker"}},"id":"1019","type":"Grid"},{"attributes":{"below":[{"id":"1010","type":"LinearAxis"}],"left":[{"id":"1015","type":"LinearAxis"}],"renderers":[{"id":"1010","type":"LinearAxis"},{"id":"1014","type":"Grid"},{"id":"1015","type":"LinearAxis"},{"id":"1019","type":"Grid"},{"id":"1028","type":"BoxAnnotation"},{"id":"1038","type":"GlyphRenderer"}],"title":{"id":"1040","type":"Title"},"toolbar":{"id":"1026","type":"Toolbar"},"x_range":{"id":"1002","type":"DataRange1d"},"x_scale":{"id":"1006","type":"LinearScale"},"y_range":{"id":"1004","type":"DataRange1d"},"y_scale":{"id":"1008","type":"LinearScale"}},"id":"1001","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"1044","type":"BasicTickFormatter"},{"attributes":{"data_source":{"id":"1035","type":"ColumnDataSource"},"glyph":{"id":"1036","type":"Circle"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1037","type":"Circle"},"selection_glyph":null,"view":{"id":"1039","type":"CDSView"}},"id":"1038","type":"GlyphRenderer"},{"attributes":{"callback":null,"data":{"x":[1,2,5,6,7],"y":[3,4,7,8,9]},"selected":{"id":"1047","type":"Selection"},"selection_policy":{"id":"1048","type":"UnionRenderers"}},"id":"1035","type":"ColumnDataSource"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1020","type":"PanTool"},{"id":"1021","type":"WheelZoomTool"},{"id":"1022","type":"BoxZoomTool"},{"id":"1023","type":"SaveTool"},{"id":"1024","type":"ResetTool"},{"id":"1025","type":"HelpTool"}]},"id":"1026","type":"Toolbar"},{"attributes":{},"id":"1006","type":"LinearScale"},{"attributes":{},"id":"1047","type":"Selection"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"1028","type":"BoxAnnotation"},{"attributes":{"callback":null},"id":"1002","type":"DataRange1d"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"1037","type":"Circle"},{"attributes":{},"id":"1008","type":"LinearScale"},{"attributes":{},"id":"1048","type":"UnionRenderers"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"1036","type":"Circle"},{"attributes":{},"id":"1020","type":"PanTool"},{"attributes":{"formatter":{"id":"1044","type":"BasicTickFormatter"},"plot":{"id":"1001","subtype":"Figure","type":"Plot"},"ticker":{"id":"1011","type":"BasicTicker"}},"id":"1010","type":"LinearAxis"},{"attributes":{"source":{"id":"1035","type":"ColumnDataSource"}},"id":"1039","type":"CDSView"},{"attributes":{},"id":"1021","type":"WheelZoomTool"},{"attributes":{},"id":"1011","type":"BasicTicker"}],"root_ids":["1001"]},"title":"Bokeh Application","version":"1.0.4"}}
</script>
<script type="text/javascript">
    (function() {
    var fn = function() {
        Bokeh.safely(function() {
        (function(root) {
            function embed_document(root) {
            
            var docs_json = document.getElementById('1112').textContent;
            var render_items = [{"docid":"bd9b9da1-a044-454d-a80d-b81d6bdf734e","roots":{"1001":"409a6f0d-0035-44f0-aeff-7d5b10db7214"}}];
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


## wrap-up

- script의 경우에도 문제없이 됩니다 하하하핫.
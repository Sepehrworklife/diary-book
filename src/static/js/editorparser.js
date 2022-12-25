/**
 * Minified by jsDelivr using Terser v5.3.5.
 * Original file: /npm/editorjs-parser@1.5.3/build/Parser.browser.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
function _classCallCheck(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function _defineProperties(e,t){for(var r=0;r<t.length;r++){var a=t[r];a.enumerable=a.enumerable||!1,a.configurable=!0,"value"in a&&(a.writable=!0),Object.defineProperty(e,a.key,a)}}function _createClass(e,t,r){return t&&_defineProperties(e.prototype,t),r&&_defineProperties(e,r),e}function _defineProperty(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function _typeof(e){return(_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}var edjsParser=function(){"use strict";var e=function(e){return e&&"object"===_typeof(e)&&!Array.isArray(e)},t=function t(r,a){var n=Object.assign({},r);return e(r)&&e(a)&&Object.keys(a).forEach((function(c){e(a[c])&&c in r?n[c]=t(r[c],a[c]):Object.assign(n,_defineProperty({},c,a[c]))})),n},r={youtube:'<div class="embed"><iframe class="embed-youtube" frameborder="0" src="<%data.embed%>" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen <%data.length%>></iframe></div>',twitter:'<blockquote class="twitter-tweet" class="embed-twitter" <%data.length%>><a href="<%data.source%>"></a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"><\/script>',instagram:'<blockquote class="instagram-media" <%data.length%>><a href="<%data.embed%>/captioned"></a></blockquote><script async defer src="//www.instagram.com/embed.js"><\/script>',codepen:'<div class="embed"><iframe <%data.length%> scrolling="no" src="<%data.embed%>" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true"></iframe></div>',defaultMarkup:'<div class="embed"><iframe src="<%data.embed%>" <%data.length%> class="embed-unknown" allowfullscreen="true" frameborder="0" ></iframe></div>'},a={paragraph:function(e,t){return'<p class="'.concat(t.paragraph.pClass,'"> ').concat(e.text," </p>")},header:function(e){return"<h".concat(e.level,">").concat(e.text,"</h").concat(e.level,">")},list:function(e){var t="ordered"===e.style?"ol":"ul",r=e.items.reduce((function(e,t){return e+"<li>".concat(t,"</li>")}),"");return"<".concat(t,">").concat(r,"</").concat(t,">")},quote:function(e,t){var r="";return t.quote.applyAlignment&&(r='style="text-align: '.concat(e.alignment,';"')),"<blockquote ".concat(r,"><p>").concat(e.text,"</p><cite>").concat(e.caption,"</cite></blockquote>")},table:function(e){var t=e.content.map((function(e){return"<tr>".concat(e.reduce((function(e,t){return e+"<td>".concat(t,"</td>")}),""),"</tr>")}));return"<table><tbody>".concat(t.join(""),"</tbody></table>")},image:function(e,t){var r,a="".concat(e.stretched?"img-fullwidth":""," ").concat(e.withBorder?"img-border":""," ").concat(e.withBackground?"img-bg":""),n=t.image.imgClass||"";if(r=e.url?e.url:"absolute"===t.image.path?e.file.url:t.image.path.replace(/<(.+)>/,(function(t,r){return e.file[r]})),"img"===t.image.use)return'<img class="'.concat(a," ").concat(n,'" src="').concat(r,'" alt="').concat(e.caption,'">');if("figure"===t.image.use){var c=t.image.figureClass||"",o=t.image.figCapClass||"";return'<figure class="'.concat(c,'"><img class="').concat(n," ").concat(a,'" src="').concat(r,'" alt="').concat(e.caption,'"><figcaption class="').concat(o,'">').concat(e.caption,"</figcaption></figure>")}},code:function(e,t){var r=function(e){return(e=(e=e.replace(/&/g,"&amp;")).replace(/</g,"&lt;")).replace(/>/g,"&gt;")}(e.code);return'<pre><code class="'.concat(t.code.codeBlockClass,'">').concat(r,"</code></pre>")},raw:function(e){return e.html},delimiter:function(e){return"<br />"},embed:function(e,t){t.embed.useProvidedLength?e.length='width="'.concat(e.width,'" height="').concat(e.height,'"'):e.length="";var r=new RegExp(/<%data\.(.+?)%>/,"gm");return t.embedMarkups[e.service]?t.embedMarkups[e.service].replace(r,(function(t,r){return e[r]})):t.embedMarkups.defaultMarkup.replace(r,(function(t,r){return e[r]}))}},n={image:{use:"figure",imgClass:"img",figureClass:"fig-img",figCapClass:"fig-cap",path:"absolute"},paragraph:{pClass:"paragraph"},code:{codeBlockClass:"code-block"},embed:{useProvidedLength:!1},quote:{applyAlignment:!1}};return function(){function e(){var c=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},o=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},i=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{};_classCallCheck(this,e),this.config=t(n,c),this.config.embedMarkups=Object.assign(r,i),this.parsers=Object.assign(a,o)}return _createClass(e,[{key:"parse",value:function(e){var t=this;return e.blocks.map((function(e){var r=t.parseBlock(e);return r instanceof Error?"":r})).join("")}},{key:"parseBlock",value:function(e){if(!this.parsers[e.type])return new Error("".concat(e.type," is not supported! Define your own custom function."));try{return this.parsers[e.type](e.data,this.config)}catch(e){return e}}}]),e}()}();
//# sourceMappingURL=/sm/cd5765d1c12a262245b6181385d19559272eed400ac2c73b7aa0b6e47cf56cf1.map
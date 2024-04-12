import urllib.request
import os, sys, re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

import shutup
shutup.please()


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def create_new_page():


    opener = urllib.request.FancyURLopener({})
    url = "http://localhost:8000/cut/18/"
    f = opener.open(url)
    content = str(f.read())

    # print(content)

    base = f'''
<!DOCTYPE html>
<!-- saved from url=(0029)http://localhost:8000/cut/18/ -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style type="text/css">:host,:root{{--fa-font-solid:normal 900 1em/1 "Font Awesome 6 Solid";--fa-font-regular:normal 400 1em/1 "Font Awesome 6 Regular";--fa-font-light:normal 300 1em/1 "Font Awesome 6 Light";--fa-font-thin:normal 100 1em/1 "Font Awesome 6 Thin";--fa-font-duotone:normal 900 1em/1 "Font Awesome 6 Duotone";--fa-font-sharp-solid:normal 900 1em/1 "Font Awesome 6 Sharp";--fa-font-sharp-regular:normal 400 1em/1 "Font Awesome 6 Sharp";--fa-font-sharp-light:normal 300 1em/1 "Font Awesome 6 Sharp";--fa-font-sharp-thin:normal 100 1em/1 "Font Awesome 6 Sharp";--fa-font-brands:normal 400 1em/1 "Font Awesome 6 Brands"}}svg:not(:host).svg-inline--fa,svg:not(:root).svg-inline--fa{{overflow:visible;box-sizing:content-box}}.svg-inline--fa{{display:var(--fa-display,inline-block);height:1em;overflow:visible;vertical-align:-.125em}}.svg-inline--fa.fa-2xs{{vertical-align:.1em}}.svg-inline--fa.fa-xs{{vertical-align:0}}.svg-inline--fa.fa-sm{{vertical-align:-.0714285705em}}.svg-inline--fa.fa-lg{{vertical-align:-.2em}}.svg-inline--fa.fa-xl{{vertical-align:-.25em}}.svg-inline--fa.fa-2xl{{vertical-align:-.3125em}}.svg-inline--fa.fa-pull-left{{margin-right:var(--fa-pull-margin,.3em);width:auto}}.svg-inline--fa.fa-pull-right{{margin-left:var(--fa-pull-margin,.3em);width:auto}}.svg-inline--fa.fa-li{{width:var(--fa-li-width,2em);top:.25em}}.svg-inline--fa.fa-fw{{width:var(--fa-fw-width,1.25em)}}.fa-layers svg.svg-inline--fa{{bottom:0;left:0;margin:auto;position:absolute;right:0;top:0}}.fa-layers-counter,.fa-layers-text{{display:inline-block;position:absolute;text-align:center}}.fa-layers{{display:inline-block;height:1em;position:relative;text-align:center;vertical-align:-.125em;width:1em}}.fa-layers svg.svg-inline--fa{{-webkit-transform-origin:center center;transform-origin:center center}}.fa-layers-text{{left:50%;top:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);-webkit-transform-origin:center center;transform-origin:center center}}.fa-layers-counter{{background-color:var(--fa-counter-background-color,#ff253a);border-radius:var(--fa-counter-border-radius,1em);box-sizing:border-box;color:var(--fa-inverse,#fff);line-height:var(--fa-counter-line-height,1);max-width:var(--fa-counter-max-width,5em);min-width:var(--fa-counter-min-width,1.5em);overflow:hidden;padding:var(--fa-counter-padding,.25em .5em);right:var(--fa-right,0);text-overflow:ellipsis;top:var(--fa-top,0);-webkit-transform:scale(var(--fa-counter-scale,.25));transform:scale(var(--fa-counter-scale,.25));-webkit-transform-origin:top right;transform-origin:top right}}.fa-layers-bottom-right{{bottom:var(--fa-bottom,0);right:var(--fa-right,0);top:auto;-webkit-transform:scale(var(--fa-layers-scale,.25));transform:scale(var(--fa-layers-scale,.25));-webkit-transform-origin:bottom right;transform-origin:bottom right}}.fa-layers-bottom-left{{bottom:var(--fa-bottom,0);left:var(--fa-left,0);right:auto;top:auto;-webkit-transform:scale(var(--fa-layers-scale,.25));transform:scale(var(--fa-layers-scale,.25));-webkit-transform-origin:bottom left;transform-origin:bottom left}}.fa-layers-top-right{{top:var(--fa-top,0);right:var(--fa-right,0);-webkit-transform:scale(var(--fa-layers-scale,.25));transform:scale(var(--fa-layers-scale,.25));-webkit-transform-origin:top right;transform-origin:top right}}.fa-layers-top-left{{left:var(--fa-left,0);right:auto;top:var(--fa-top,0);-webkit-transform:scale(var(--fa-layers-scale,.25));transform:scale(var(--fa-layers-scale,.25));-webkit-transform-origin:top left;transform-origin:top left}}.fa-1x{{font-size:1em}}.fa-2x{{font-size:2em}}.fa-3x{{font-size:3em}}.fa-4x{{font-size:4em}}.fa-5x{{font-size:5em}}.fa-6x{{font-size:6em}}.fa-7x{{font-size:7em}}.fa-8x{{font-size:8em}}.fa-9x{{font-size:9em}}.fa-10x{{font-size:10em}}.fa-2xs{{font-size:.625em;line-height:.1em;vertical-align:.225em}}.fa-xs{{font-size:.75em;line-height:.0833333337em;vertical-align:.125em}}.fa-sm{{font-size:.875em;line-height:.0714285718em;vertical-align:.0535714295em}}.fa-lg{{font-size:1.25em;line-height:.05em;vertical-align:-.075em}}.fa-xl{{font-size:1.5em;line-height:.0416666682em;vertical-align:-.125em}}.fa-2xl{{font-size:2em;line-height:.03125em;vertical-align:-.1875em}}.fa-fw{{text-align:center;width:1.25em}}.fa-ul{{list-style-type:none;margin-left:var(--fa-li-margin,2.5em);padding-left:0}}.fa-ul>li{{position:relative}}.fa-li{{left:calc(var(--fa-li-width,2em) * -1);position:absolute;text-align:center;width:var(--fa-li-width,2em);line-height:inherit}}.fa-border{{border-color:var(--fa-border-color,#eee);border-radius:var(--fa-border-radius,.1em);border-style:var(--fa-border-style,solid);border-width:var(--fa-border-width,.08em);padding:var(--fa-border-padding,.2em .25em .15em)}}.fa-pull-left{{float:left;margin-right:var(--fa-pull-margin,.3em)}}.fa-pull-right{{float:right;margin-left:var(--fa-pull-margin,.3em)}}.fa-beat{{-webkit-animation-name:fa-beat;animation-name:fa-beat;-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,ease-in-out);animation-timing-function:var(--fa-animation-timing,ease-in-out)}}.fa-bounce{{-webkit-animation-name:fa-bounce;animation-name:fa-bounce;-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,cubic-bezier(.28,.84,.42,1));animation-timing-function:var(--fa-animation-timing,cubic-bezier(.28,.84,.42,1))}}.fa-fade{{-webkit-animation-name:fa-fade;animation-name:fa-fade;-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1));animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1))}}.fa-beat-fade{{-webkit-animation-name:fa-beat-fade;animation-name:fa-beat-fade;-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1));animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1))}}.fa-flip{{-webkit-animation-name:fa-flip;animation-name:fa-flip;-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,ease-in-out);animation-timing-function:var(--fa-animation-timing,ease-in-out)}}.fa-shake{{-webkit-animation-name:fa-shake;animation-name:fa-shake;-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,linear);animation-timing-function:var(--fa-animation-timing,linear)}}.fa-spin{{-webkit-animation-name:fa-spin;animation-name:fa-spin;-webkit-animation-delay:var(--fa-animation-delay,0s);animation-delay:var(--fa-animation-delay,0s);-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,2s);animation-duration:var(--fa-animation-duration,2s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,linear);animation-timing-function:var(--fa-animation-timing,linear)}}.fa-spin-reverse{{--fa-animation-direction:reverse}}.fa-pulse,.fa-spin-pulse{{-webkit-animation-name:fa-spin;animation-name:fa-spin;-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:var(--fa-animation-timing,steps(8));animation-timing-function:var(--fa-animation-timing,steps(8))}}@media (prefers-reduced-motion:reduce){{.fa-beat,.fa-beat-fade,.fa-bounce,.fa-fade,.fa-flip,.fa-pulse,.fa-shake,.fa-spin,.fa-spin-pulse{{-webkit-animation-delay:-1ms;animation-delay:-1ms;-webkit-animation-duration:1ms;animation-duration:1ms;-webkit-animation-iteration-count:1;animation-iteration-count:1;-webkit-transition-delay:0s;transition-delay:0s;-webkit-transition-duration:0s;transition-duration:0s}}}}@-webkit-keyframes fa-beat{{0%,90%{{-webkit-transform:scale(1);transform:scale(1)}}45%{{-webkit-transform:scale(var(--fa-beat-scale,1.25));transform:scale(var(--fa-beat-scale,1.25))}}}}@keyframes fa-beat{{0%,90%{{-webkit-transform:scale(1);transform:scale(1)}}45%{{-webkit-transform:scale(var(--fa-beat-scale,1.25));transform:scale(var(--fa-beat-scale,1.25))}}}}@-webkit-keyframes fa-bounce{{0%{{-webkit-transform:scale(1,1) translateY(0);transform:scale(1,1) translateY(0)}}10%{{-webkit-transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0);transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0)}}30%{{-webkit-transform:scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1)) translateY(var(--fa-bounce-height,-.5em));transform:scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1)) translateY(var(--fa-bounce-height,-.5em))}}50%{{-webkit-transform:scale(var(--fa-bounce-land-scale-x,1.05),var(--fa-bounce-land-scale-y,.95)) translateY(0);transform:scale(var(--fa-bounce-land-scale-x,1.05),var(--fa-bounce-land-scale-y,.95)) translateY(0)}}57%{{-webkit-transform:scale(1,1) translateY(var(--fa-bounce-rebound,-.125em));transform:scale(1,1) translateY(var(--fa-bounce-rebound,-.125em))}}64%{{-webkit-transform:scale(1,1) translateY(0);transform:scale(1,1) translateY(0)}}100%{{-webkit-transform:scale(1,1) translateY(0);transform:scale(1,1) translateY(0)}}}}@keyframes fa-bounce{{0%{{-webkit-transform:scale(1,1) translateY(0);transform:scale(1,1) translateY(0)}}10%{{-webkit-transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0);transform:scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9)) translateY(0)}}30%{{-webkit-transform:scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1)) translateY(var(--fa-bounce-height,-.5em));transform:scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1)) translateY(var(--fa-bounce-height,-.5em))}}50%{{-webkit-transform:scale(var(--fa-bounce-land-scale-x,1.05),var(--fa-bounce-land-scale-y,.95)) translateY(0);transform:scale(var(--fa-bounce-land-scale-x,1.05),var(--fa-bounce-land-scale-y,.95)) translateY(0)}}57%{{-webkit-transform:scale(1,1) translateY(var(--fa-bounce-rebound,-.125em));transform:scale(1,1) translateY(var(--fa-bounce-rebound,-.125em))}}64%{{-webkit-transform:scale(1,1) translateY(0);transform:scale(1,1) translateY(0)}}100%{{-webkit-transform:scale(1,1) translateY(0);transform:scale(1,1) translateY(0)}}}}@-webkit-keyframes fa-fade{{50%{{opacity:var(--fa-fade-opacity,.4)}}}}@keyframes fa-fade{{50%{{opacity:var(--fa-fade-opacity,.4)}}}}@-webkit-keyframes fa-beat-fade{{0%,100%{{opacity:var(--fa-beat-fade-opacity,.4);-webkit-transform:scale(1);transform:scale(1)}}50%{{opacity:1;-webkit-transform:scale(var(--fa-beat-fade-scale,1.125));transform:scale(var(--fa-beat-fade-scale,1.125))}}}}@keyframes fa-beat-fade{{0%,100%{{opacity:var(--fa-beat-fade-opacity,.4);-webkit-transform:scale(1);transform:scale(1)}}50%{{opacity:1;-webkit-transform:scale(var(--fa-beat-fade-scale,1.125));transform:scale(var(--fa-beat-fade-scale,1.125))}}}}@-webkit-keyframes fa-flip{{50%{{-webkit-transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg));transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg))}}}}@keyframes fa-flip{{50%{{-webkit-transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg));transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg))}}}}@-webkit-keyframes fa-shake{{0%{{-webkit-transform:rotate(-15deg);transform:rotate(-15deg)}}4%{{-webkit-transform:rotate(15deg);transform:rotate(15deg)}}24%,8%{{-webkit-transform:rotate(-18deg);transform:rotate(-18deg)}}12%,28%{{-webkit-transform:rotate(18deg);transform:rotate(18deg)}}16%{{-webkit-transform:rotate(-22deg);transform:rotate(-22deg)}}20%{{-webkit-transform:rotate(22deg);transform:rotate(22deg)}}32%{{-webkit-transform:rotate(-12deg);transform:rotate(-12deg)}}36%{{-webkit-transform:rotate(12deg);transform:rotate(12deg)}}100%,40%{{-webkit-transform:rotate(0);transform:rotate(0)}}}}@keyframes fa-shake{{0%{{-webkit-transform:rotate(-15deg);transform:rotate(-15deg)}}4%{{-webkit-transform:rotate(15deg);transform:rotate(15deg)}}24%,8%{{-webkit-transform:rotate(-18deg);transform:rotate(-18deg)}}12%,28%{{-webkit-transform:rotate(18deg);transform:rotate(18deg)}}16%{{-webkit-transform:rotate(-22deg);transform:rotate(-22deg)}}20%{{-webkit-transform:rotate(22deg);transform:rotate(22deg)}}32%{{-webkit-transform:rotate(-12deg);transform:rotate(-12deg)}}36%{{-webkit-transform:rotate(12deg);transform:rotate(12deg)}}100%,40%{{-webkit-transform:rotate(0);transform:rotate(0)}}}}@-webkit-keyframes fa-spin{{0%{{-webkit-transform:rotate(0);transform:rotate(0)}}100%{{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}}}@keyframes fa-spin{{0%{{-webkit-transform:rotate(0);transform:rotate(0)}}100%{{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}}}.fa-rotate-90{{-webkit-transform:rotate(90deg);transform:rotate(90deg)}}.fa-rotate-180{{-webkit-transform:rotate(180deg);transform:rotate(180deg)}}.fa-rotate-270{{-webkit-transform:rotate(270deg);transform:rotate(270deg)}}.fa-flip-horizontal{{-webkit-transform:scale(-1,1);transform:scale(-1,1)}}.fa-flip-vertical{{-webkit-transform:scale(1,-1);transform:scale(1,-1)}}.fa-flip-both,.fa-flip-horizontal.fa-flip-vertical{{-webkit-transform:scale(-1,-1);transform:scale(-1,-1)}}.fa-rotate-by{{-webkit-transform:rotate(var(--fa-rotate-angle,none));transform:rotate(var(--fa-rotate-angle,none))}}.fa-stack{{display:inline-block;vertical-align:middle;height:2em;position:relative;width:2.5em}}.fa-stack-1x,.fa-stack-2x{{bottom:0;left:0;margin:auto;position:absolute;right:0;top:0;z-index:var(--fa-stack-z-index,auto)}}.svg-inline--fa.fa-stack-1x{{height:1em;width:1.25em}}.svg-inline--fa.fa-stack-2x{{height:2em;width:2.5em}}.fa-inverse{{color:var(--fa-inverse,#fff)}}.fa-sr-only,.sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border-width:0}}.fa-sr-only-focusable:not(:focus),.sr-only-focusable:not(:focus){{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border-width:0}}.svg-inline--fa .fa-primary{{fill:var(--fa-primary-color,currentColor);opacity:var(--fa-primary-opacity,1)}}.svg-inline--fa .fa-secondary{{fill:var(--fa-secondary-color,currentColor);opacity:var(--fa-secondary-opacity,.4)}}.svg-inline--fa.fa-swap-opacity .fa-primary{{opacity:var(--fa-secondary-opacity,.4)}}.svg-inline--fa.fa-swap-opacity .fa-secondary{{opacity:var(--fa-primary-opacity,1)}}.svg-inline--fa mask .fa-primary,.svg-inline--fa mask .fa-secondary{{fill:#000}}.fa-duotone.fa-inverse,.fad.fa-inverse{{color:var(--fa-inverse,#fff)}}</style><link rel="preconnect" href="https://fonts.googleapis.com/">
    <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin="">
    <link href="./b003_files/css2" rel="stylesheet">
    <link href="./b003_files/css2(1)" rel="stylesheet">
    
    <link rel="stylesheet" href="./b003_files/jalalidatepicker.min.css">
    <link rel="stylesheet" href="./b003_files/output.css" type="text/css">
    <link rel="stylesheet" href="./b003_files/custom.css" type="text/css">
    <script type="text/javascript" src="./b003_files/jalalidatepicker.min.js.download"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com/">
    <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin="">
    <link href="./b003_files/css2(2)" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap" rel="stylesheet">

<script src="./b003_files/script.js.download" type="text/javascript"></script>
<script src="./b003_files/fontawesome.js.download"></script>
<script src="./b003_files/solid.js.download"></script>
<script src="./b003_files/brands.js.download"></script>
<script src="./b003_files/regular.js.download"></script>
    <title>Accounting Home</title>
  </head>
  <body>
    <nav class="bg-white bg-opacity-30 backdrop-filter backdrop-blur-lg px-2 sm:px-4 py-1  fixed w-full z-20 top-0 left-0 border-b border-gray-200 dark:border-gray-600">
  <div class="container flex flex-wrap items-center justify-between mx-auto">
    <a href="http://localhost:8000/" class="flex items-center">
      <!-- <img
        src="https://flowbite.com/docs/images/logo.svg"
        class="h-6 mr-3 sm:h-9"
        alt="Flowbite Logo" /> -->
      <span class="font-vazir self-center text-xl font-semibold whitespace-nowrap dark:text-white">حسابداری</span>
    </a>
    <div class="flex md:order-2">
      <!-- <button
        type="button"
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-1 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        Get started
      </button> -->
      <button data-collapse-toggle="navbar-sticky" type="button" class="bg-opacity-0 inline-flex items-center p-2 text-sm text-gray-500 rounded-lg md:hidden focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400  dark:focus:ring-gray-600" aria-controls="navbar-sticky" aria-expanded="false">
        <span class="sr-only">Open main menu</span>
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path>
        </svg>
      </button>
    </div>
    <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
      <!-- <ul class="flex flex-col p-2 mt-1 border border-gray-100 rounded-lg md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0  dark:border-gray-700">
        <li>
          <a href="http://localhost:8000/" class="font-vazir text-lg block py-2 pl-3 pr-4 text-gray-700 rounded  md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400  dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700" aria-current="page">خانه</a>
        </li>
        <li>
          <a href="http://localhost:8000/admin/" class="font-vazir text-lg block py-2 pl-3 pr-4 text-gray-700 rounded  md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">ادمین</a>
        </li>
        <li>
          <a href="http://localhost:8000/reciept/" class="font-vazir text-lg block py-2 pl-3 pr-4 text-gray-700 rounded  md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400  dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">قبض</a>
        </li>
        <li>
          <a href="http://localhost:8000/user/" class="font-vazir text-lg block py-2 pl-3 pr-4 text-gray-700 rounded  md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">کاربر</a>
        </li>
        <li>
          <a href="http://localhost:8000/cut/" class="font-vazir text-lg block py-2 pl-3 pr-4 text-gray-700 rounded  md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">برش</a>
        </li>
        <li>
          <a href="http://localhost:8000/clothroll/" class="font-vazir text-lg block py-2 pl-3 pr-4 text-gray-700 rounded  md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">طاقه‌‌ها</a>
        </li>
      </ul> -->
    </div>
  </div>
</nav>



{content}


    
  
  <script src="./b003_files/flowbite.min.js.download"></script>
</body></html>
'''
    new_file = open("b001.html", "w")
    new_file.write(content)
    new_file.close()





def savePage(url, pagepath='page'):
    def savenRename(soup, pagefolder, session, url, tag, inner):
        if not os.path.exists(pagefolder): # create only once
            os.mkdir(pagefolder)
        for res in soup.findAll(tag):   # images, css, etc..
            if res.has_attr(inner): # check inner tag (file object) MUST exists  
                try:
                    filename, ext = os.path.splitext(os.path.basename(res[inner])) # get name and extension
                    try:
                      filename = re.sub(r'\W+', '', filename) + ext # clean special chars from name
                    except SyntaxWarning:
                      ...
                    fileurl = urljoin(url, res.get(inner))
                    filepath = os.path.join(pagefolder, filename)
                    # rename html ref so can move html and folder of files anywhere
                    res[inner] = os.path.join(os.path.basename(pagefolder), filename)
                    if not os.path.isfile(filepath): # was not downloaded
                        with open(filepath, 'wb') as file:
                            filebin = session.get(fileurl)
                            file.write(filebin.content)
                except Exception as exc:
                    print(exc, file=sys.stderr)
    session = requests.Session()
    #... whatever other requests config you need here
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    path, _ = os.path.splitext(pagepath)
    # pagefolder = path+'_files' # page contents folder
    pagefolder = 'files' # page contents folder
    tags_inner = {'img': 'src', 'link': 'href', 'script': 'src'} # tag&inner tags to grab
    for tag, inner in tags_inner.items(): # saves resource files and rename refs
        savenRename(soup, pagefolder, session, url, tag, inner)
    with open(path+'.html', 'wb') as file: # saves modified html doc
        file.write(soup.prettify('utf-8'))

while True: 
  cut_code = str(input("Enter the Cut Code to download (to stop the program #n): "))
  if cut_code == "#n":
    break
  
  if len(cut_code) == 4:
    savePage(f'http://localhost:8000/cut/{cut_code}/', cut_code)
    print(f"\33[32m[{cut_code}] : download finished.\033[0m ")
  else:
    print(f"\33[33m[{cut_code}] : Invalid code!\033[0m ")
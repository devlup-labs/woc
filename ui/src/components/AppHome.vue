<template>

<div>
<div id="div1">Winter</div><br>
<div id="div2">Of</div><br>
<div id="div3">Code</div><br>
<div id="div4">2018</div><br>
<div id="div5">IITJ</div><br>
</div>
</template>

<script>
  import AppNavbar from './AppNavbar'
  import AppFooter from './AppFooter'

  export default {
    components: {AppNavbar, AppFooter}
  }
</script>

<style scoped>
div {
    width: 50px;
    height: 100px;
    -webkit-transition: width 25s; /* Safari */
    transition: width 2s;
}

/* For Safari 3.1 to 6.0 */
#div1 {-webkit-transition-timing-function: ease-out;
        background:yellow;
        color:white;
         font-size:50px;}
#div2 {-webkit-transition-timing-function: ease-out;
          background:#27C807;
          color:white;
         font-size:50px;}
#div3 {-webkit-transition-timing-function: ease-out;
         background:#E70D76;
         color:white;
         font-size:50px;}
#div4 {-webkit-transition-timing-function: ease-out;
         background:#19A9B8;
         color:white;
         font-size:50px;}
#div5 {-webkit-transition-timing-function: ease-out;
         background:#F56D15;
         color:white;
         font-size:50px;}

/* Standard syntax */
#div1 {transition-timing-function: ease-out;}
#div2 {transition-timing-function: ease-out;}
#div3 {transition-timing-function: ease-out;}
#div4 {transition-timing-function: ease-out;}
#div5 {transition-timing-function: ease-out;}

div:hover {
    width: 300px;
}
</style>
</style>

<template>
  <v-card flat>
    <v-card-title class="pb-0 pt-0" primary-title>
      <div class="display-1 text-md-center">Timeline</div>
    </v-card-title>
    <v-card-text>
      <!-- <v-timeline v-if="timeline.length != 0" :dense='$vuetify.breakpoint.smAndDown'>
        <v-timeline-item v-for="(t,index) in timeline" :key="index" ,fill-dot='' :value='index%2 === 0 ? "right":"left"'>
        </v-timeline-item>
      </v-timeline> -->
      <div class="vertical-timeline vertical-timeline vertical-timeline--animate vertical-timeline--two-columns">
      <div v-for="(t,index) in timeline" :key="index" id="" class="vertical-timeline-element--work vertical-timeline-element">
        <span class="vertical-timeline-element-icon is-hidden" style="background: rgb(46, 204, 113); color: rgb(255, 255, 255);">
          <svg xmlns="http://www.w3.org/2000/svg" width="31" height="31" fill="#fff" viewBox="0 0 24 24"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-1.834 9.686l-4.166.575 3.032 2.914-.74 4.139 3.708-1.982 3.708 1.983-.74-4.139 3.032-2.915-4.166-.575-1.834-3.784-1.834 3.784z"></path></svg>
        </span>
        <div class="vertical-timeline-element-content is-hidden" style="background: rgb(46, 204, 113); color: rgb(255, 255, 255);">
          <div class="vertical-timeline-element-content-arrow" style="border-right: 7px solid rgb(46, 204, 113);"></div>
          <h3 class="vertical-timeline-element-title">{{t.title}}</h3>
          <p id="vertical-timeline-element-description">{{t.description}}</p>
          <span class="vertical-timeline-element-date">{{getEventTimestamp(t)}}</span>
        </div>
      </div>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
  import inViewport from 'jquery'
  const $ = require('jquery')
// We declare it globally
window.$ = $
  export default {
    name: 'Timeline',
    data () {
      return {
        e1: 1,
        timeline: []
      }
    },
    methods: {
      nextTimeline (n) {
        if (n === this.timeline.length) {
          this.e1 = 1
        } else {
          this.e1 = n + 1
        }
      },
      getEventTimestamp (event) {
        if (event.startTime.toLocaleString() === event.endTime.toLocaleString()) {
          return event.startTime.toDateString('en-in')
        } else {
          return `${event.startTime.toDateString('en-in')} to ${event.endTime.toDateString('en-in')}`
        }
      },
      fetchTimelines () {
        this.loading = true
        fetch(
          'https://spreadsheets.google.com/feeds/list/1YdkA5vEDqFcEHinWIn5ojzCbdgUBKVIJ1yQEScZ8OOQ/od6/public/values?alt=json'
        )
        .then(e =>
          e.json().then(e => {
            e = e.feed.entry
            e.forEach(ele => {
              this.timeline.push(
                {
                  startTime: new Date(ele.gsx$starttime['$t']),
                  endTime: new Date(ele.gsx$endtime['$t']),
                  title: ele.gsx$title['$t'],
                  description: ele.gsx$description['$t']
                }
            )
            })
          }
          )
        )
        .finally(() => (this.loading = false))
      }
    },
    mounted () {
      this.fetchTimelines()
    }
  }
  $(window).on('scroll', function () {
    $('.vertical-timeline-element-content').each(function () {
      var isHidden = $(this).hasClass('is-hidden')
      if (isHidden && inViewport(this)) {
        $(this).removeClass('is-hidden').addClass('bounce-in')
      }
    })
    $('.vertical-timeline-element-icon').each(function () {
      var isHidden = $(this).hasClass('is-hidden')

      if (isHidden && inViewport(this)) {
        $(this).removeClass('is-hidden').addClass('bounce-in')
      }
    })
  })
</script>

<style scoped>
 .v-stepper {
	box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.2), 0 0 0 0 rgba(0, 0, 0, 0.14), 0 0 0 0 rgba(0, 0, 0, 0.12);
}

.vertical-timeline * {
	box-sizing: border-box;
}

.vertical-timeline {
	width: 95%;
	max-width: 1170px;
	margin: 0 auto;
	position: relative;
	padding: 2em 0;
}

a {
	text-decoration: none;
}

.vertical-timeline::before {
	/* this is the vertical line */
	content: '';
	position: absolute;
	top: 0;
	height: 100%;
	width: 4px;
	background: white;
}

h3 {
	font-weight: 500;
}

h4 {
	font-weight: 300;
	font-style: italic;
	margin-bottom: 0;
	padding-bottom: 0;
}

.vertical-paragraph {
	padding-top: 0px;
	margin-top: 0px;
	margin-bottom: 0px;
	padding-bottom: 0px;
	color: black;
	font-weight: 200;
}

@media only screen and (min-width: 1170px) {
	.vertical-timeline.vertical-timeline--two-columns {
		width: 90%;
	}
	.vertical-timeline.vertical-timeline--two-columns:before {
		left: 50%;
		margin-left: -2px;
	}
}

@media only screen and (min-width: 320px) {
	.vertical-timeline-element-title {
		font-size: 20px;
	}
	.vertical-timeline-element-subtitle {
		font-size: 18px;
	}
	.vertical-timeline-element--work {
		padding: 0px;
	}
}

.vertical-timeline-element-date {
	padding: .8em 0;
	opacity: .7;
	display: inline-block;
	position: absolute;
	width: 100%;
	left: 124%;
	top: 6px;
	color: #222;
	font-size: 1.4rem;
	font-weight: bold;
}

.vertical-timeline * {
	box-sizing: border-box
}

.vertical-timeline {
	width: 95%;
	max-width: 1170px;
	margin: 0 auto;
	position: relative;
	padding: 2em 0
}

.vertical-timeline::after {
	content: '';
	display: table;
	clear: both
}

.vertical-timeline::before {
	content: '';
	position: absolute;
	top: 0;
	left: 18px;
	height: 100%;
	width: 4px;
	background: #fff
}

@media only screen and (min-width:1170px) {
	.vertical-timeline.vertical-timeline--two-columns {
		width: 90%
	}
	.vertical-timeline.vertical-timeline--two-columns:before {
		left: 50%;
		margin-left: -2px
	}
}

.vertical-timeline-element {
	position: relative;
	margin: 2em 0
}

.vertical-timeline-element>div {
	min-height: 1px
}

.vertical-timeline-element:after {
	content: "";
	display: table;
	clear: both
}

.vertical-timeline-element:first-child {
	margin-top: 0
}

.vertical-timeline-element:last-child {
	margin-bottom: 0
}

@media only screen and (min-width:1170px) {
	.vertical-timeline-element {
		margin: 4em 0
	}
	.vertical-timeline-element:first-child {
		margin-top: 0
	}
	.vertical-timeline-element:last-child {
		margin-bottom: 0
	}
}

.vertical-timeline-element-icon {
	position: absolute;
	top: 0;
	left: 0;
	width: 40px;
	height: 40px;
	border-radius: 50%;
	box-shadow: 0 0 0 4px #fff, inset 0 2px 0 rgba(0, 0, 0, .08), 0 3px 0 4px rgba(0, 0, 0, .05);
}

.vertical-timeline-element-icon svg {
	display: block;
	width: 24px;
	height: 24px;
	position: relative;
	left: 50%;
	top: 50%;
	margin-left: -12px;
	margin-top: -12px
}

@media only screen and (min-width:1170px) {
	.vertical-timeline--two-columns .vertical-timeline-element-icon {
		width: 60px;
		height: 60px;
		left: 50%;
		margin-left: -30px;
	}
}

.vertical-timeline-element-icon {
	-webkit-transform: translateZ(0);
	-webkit-backface-visibility: hidden;
}

.vertical-timeline--animate .vertical-timeline-element-icon.is-hidden {
	visibility: hidden;
}

.vertical-timeline--animate .vertical-timeline-element-icon.bounce-in {
	visibility: visible;
	-webkit-animation: cd-bounce-1 .6s;
	-moz-animation: cd-bounce-1 .6s;
	animation: cd-bounce-1 .6s;
}

@-webkit-keyframes cd-bounce-1 {
	0% {
		opacity: 0;
		-webkit-transform: scale(.5)
	}
	60% {
		opacity: 1;
		-webkit-transform: scale(1.2)
	}
	100% {
		-webkit-transform: scale(1)
	}
}

@-moz-keyframes cd-bounce-1 {
	0% {
		opacity: 0;
		-moz-transform: scale(.5)
	}
	60% {
		opacity: 1;
		-moz-transform: scale(1.2)
	}
	100% {
		-moz-transform: scale(1)
	}
}

@keyframes cd-bounce-1 {
	0% {
		opacity: 0;
		-webkit-transform: scale(.5);
		-moz-transform: scale(.5);
		-ms-transform: scale(.5);
		-o-transform: scale(.5);
		transform: scale(.5)
	}
	60% {
		opacity: 1;
		-webkit-transform: scale(1.2);
		-moz-transform: scale(1.2);
		-ms-transform: scale(1.2);
		-o-transform: scale(1.2);
		transform: scale(1.2)
	}
	100% {
		-webkit-transform: scale(1);
		-moz-transform: scale(1);
		-ms-transform: scale(1);
		-o-transform: scale(1);
		transform: scale(1)
	}
}

.vertical-timeline-element-content {
	position: relative;
	margin-left: 60px;
	background: #fff;
	border-radius: .25em;
	padding: 1em;
	box-shadow: 0 3px 0 #ddd
}

.vertical-timeline-element--no-children .vertical-timeline-element-content {
	background: 0 0;
	box-shadow: none
}

.vertical-timeline-element-content:after {
	content: "";
	display: table;
	clear: both
}

.vertical-timeline-element-content h2 {
	color: #303e49
}

.vertical-timeline-element-content .vertical-timeline-element-date .vertical-timeline-element-content p {
	font-size: 13px;
	font-size: .8125rem;
	font-weight: 500
}

.vertical-timeline-element-content .vertical-timeline-element-date {
	display: inline-block
}

.vertical-timeline-element-content p {
	margin: 1em 0 0;
	line-height: 1.6
}

.vertical-timeline-element-title {
	margin: 0
}

.vertical-timeline-element-subtitle {
	margin: 0
}

.vertical-timeline-element-content .vertical-timeline-element-date {
	float: left;
	padding: .8em 0;
	opacity: .7
}

.vertical-timeline-element-content-arrow {
	content: '';
	position: absolute;
	top: 16px;
	right: 100%;
	height: 0;
	width: 0;
	border: 7px solid transparent;
	border-right: 7px solid #fff
}

.vertical-timeline-element--no-children .vertical-timeline-element-content-arrow {
	display: none
}

@media only screen and (min-width:468px) {
	.vertical-timeline-element-content h2 {
		font-size: 20px;
		font-size: 1.25rem
	}
	.vertical-timeline-element-content p {
		font-size: 16px;
		font-size: 1rem
	}
	.vertical-timeline-element-content .vertical-timeline-element-date {
		font-size: 14px;
		font-size: .875rem
	}
}

@media only screen and (min-width:1170px) {
	.vertical-timeline--two-columns .vertical-timeline-element-content {
		margin-left: 0;
		padding: 1.5em;
		width: 44%
	}
	.vertical-timeline--two-columns .vertical-timeline-element-content-arrow {
		top: 24px;
		left: 100%;
		transform: rotate(180deg)
	}
	.vertical-timeline--two-columns .vertical-timeline-element-content .vertical-timeline-element-date {
		position: absolute;
		width: 100%;
		left: 124%;
		top: 6px;
		font-size: 16px;
		font-size: 1rem
	}
	.vertical-timeline--two-columns .vertical-timeline-element.vertical-timeline-element--right .vertical-timeline-element-content,
	.vertical-timeline--two-columns .vertical-timeline-element:nth-child(even):not(.vertical-timeline-element--left) .vertical-timeline-element-content {
		float: right
	}
	.vertical-timeline--two-columns .vertical-timeline-element.vertical-timeline-element--right .vertical-timeline-element-content-arrow,
	.vertical-timeline--two-columns .vertical-timeline-element:nth-child(even):not(.vertical-timeline-element--left) .vertical-timeline-element-content-arrow {
		top: 24px;
		left: auto;
		right: 100%;
		transform: rotate(0)
	}
	.vertical-timeline--two-columns .vertical-timeline-element.vertical-timeline-element--right .vertical-timeline-element-content .vertical-timeline-element-date,
	.vertical-timeline--two-columns .vertical-timeline-element:nth-child(even):not(.vertical-timeline-element--left) .vertical-timeline-element-content .vertical-timeline-element-date {
		left: auto;
		right: 124%;
		text-align: right
	}
}

.vertical-timeline--animate .vertical-timeline-element-content.is-hidden {
	visibility: hidden
}

.vertical-timeline--animate .vertical-timeline-element-content.bounce-in {
	visibility: visible;
	-webkit-animation: cd-bounce-2 .6s;
	-moz-animation: cd-bounce-2 .6s;
	animation: cd-bounce-2 .6s
}

@media only screen and (min-width:1170px) {
	.vertical-timeline--two-columns.vertical-timeline--animate .vertical-timeline-element.vertical-timeline-element--right .vertical-timeline-element-content.bounce-in,
	.vertical-timeline--two-columns.vertical-timeline--animate .vertical-timeline-element:nth-child(even):not(.vertical-timeline-element--left) .vertical-timeline-element-content.bounce-in {
		-webkit-animation: cd-bounce-2-inverse .6s;
		-moz-animation: cd-bounce-2-inverse .6s;
		animation: cd-bounce-2-inverse .6s
	}
}

@media only screen and (max-width:1169px) {
	.vertical-timeline--animate .vertical-timeline-element-content.bounce-in {
		visibility: visible;
		-webkit-animation: cd-bounce-2-inverse .6s;
		-moz-animation: cd-bounce-2-inverse .6s;
		animation: cd-bounce-2-inverse .6s;
    width:43%
	}
}

@-webkit-keyframes cd-bounce-2 {
	0% {
		opacity: 0;
		-webkit-transform: translateX(-100px)
	}
	60% {
		opacity: 1;
		-webkit-transform: translateX(20px)
	}
	100% {
		-webkit-transform: translateX(0)
	}
}

@-moz-keyframes cd-bounce-2 {
	0% {
		opacity: 0;
		-moz-transform: translateX(-100px)
	}
	60% {
		opacity: 1;
		-moz-transform: translateX(20px)
	}
	100% {
		-moz-transform: translateX(0)
	}
}

@keyframes cd-bounce-2 {
	0% {
		opacity: 0;
		-webkit-transform: translateX(-100px);
		-moz-transform: translateX(-100px);
		-ms-transform: translateX(-100px);
		-o-transform: translateX(-100px);
		transform: translateX(-100px)
	}
	60% {
		opacity: 1;
		-webkit-transform: translateX(20px);
		-moz-transform: translateX(20px);
		-ms-transform: translateX(20px);
		-o-transform: translateX(20px);
		transform: translateX(20px)
	}
	100% {
		-webkit-transform: translateX(0);
		-moz-transform: translateX(0);
		-ms-transform: translateX(0);
		-o-transform: translateX(0);
		transform: translateX(0)
	}
}

@-webkit-keyframes cd-bounce-2-inverse {
	0% {
		opacity: 0;
		-webkit-transform: translateX(100px)
	}
	60% {
		opacity: 1;
		-webkit-transform: translateX(-20px)
	}
	100% {
		-webkit-transform: translateX(0)
	}
}

@-moz-keyframes cd-bounce-2-inverse {
	0% {
		opacity: 0;
		-moz-transform: translateX(100px)
	}
	60% {
		opacity: 1;
		-moz-transform: translateX(-20px)
	}
	100% {
		-moz-transform: translateX(0)
	}
}

@keyframes cd-bounce-2-inverse {
	0% {
		opacity: 0;
		-webkit-transform: translateX(100px);
		-moz-transform: translateX(100px);
		-ms-transform: translateX(100px);
		-o-transform: translateX(100px);
		transform: translateX(100px)
	}
	60% {
		opacity: 1;
		-webkit-transform: translateX(-20px);
		-moz-transform: translateX(-20px);
		-ms-transform: translateX(-20px);
		-o-transform: translateX(-20px);
		transform: translateX(-20px)
	}
	100% {
		-webkit-transform: translateX(0);
		-moz-transform: translateX(0);
		-ms-transform: translateX(0);
		-o-transform: translateX(0);
		transform: translateX(0)
	}
}
</style>

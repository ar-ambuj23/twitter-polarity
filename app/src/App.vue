<template>
  <div class="container-fluid" id="app">
	<div class="container-fluid">
		<nav class="navbar navbar-dark fixed-top">
			<div align="left" class="navbar-brand">
				<i class="fab fa-twitter"></i>
				Twitter Polarity
			</div>
			<div align=right>
				<form v-on:submit.prevent="search" class="form-inline">
				<input class="form-control mr-sm-2" type="search" placeholder="Search" v-model="search_query">
				<button class="btn btn-light my-2" type="submit"><i class="fas fa-search"></i></button>
				</form>
			</div>
		</nav>
		<div>
			<div v-if="search_active" class="row hashtag-card card">
				<div class="col-6 card-header" @click="goto(hashtag_search.url)">
					<h2>{{hashtag_search.name}}</h2>
					<div class="hashtag-desc card-text">
						Tweets:- {{hashtag_search.tweet_volume}}
						<div v-if="hashtag_search.promoted_content">Promoted Content</div>
					</div>
				</div>
				<div class="col-6 card-header" @click="hashtag_search.show=!hashtag_search.show">
					<line-chart class="small" :chartdata="chartdata_search" :options="options"></line-chart>
				</div>
				<bar-chart class="medium" v-if="hashtag_search.show" :chartdata="chartdataBar_search" :options="optionsBar"></bar-chart>
			</div>

			<div v-else :key=hashtag.name v-for="(hashtag, index) in hashtags" class="row hashtag-card card">
				<div class="col-6 card-header" @click="goto(hashtag.url)">
					<h2>{{hashtag.name}}</h2>
					<div class="hashtag-desc card-text">
						Tweets:- {{hashtag.tweet_volume}}
						<div v-if="hashtag.promoted_content">Promoted Content</div>
					</div>
				</div>
				<div class="col-6 card-header" @click="hashtag.show=!hashtag.show">
					<line-chart class="small" :chartdata="chartdata[index]" :options="options"></line-chart>
				</div>
				<bar-chart class="medium" v-if="hashtag.show" :chartdata="chartdataBar[index]" :options="optionsBar"></bar-chart>
			</div>
		</div>
	</div>
    
  </div>
</template>

<script>
import LineChart from './LineChart.vue'
import BarChart from './BarChart.vue'
export default {
name: 'App',
components: {
	'line-chart': LineChart,
	'bar-chart': BarChart
},
data(){
	return{
		search_query: "",
		search_active: false,
		hashtag_search: {},
		hashtags: [
  {
    "date_polarity_counts": [
      {
        "-1": 0.6666666666666666, 
        "0": 0.0, 
        "1": 0.3333333333333333, 
        "date": "Mon, 16 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.5
      }, 
      {
        "-1": 0.5, 
        "0": 0.5, 
        "1": 0.0, 
        "date": "Tue, 17 Nov 2020 00:00:00 GMT", 
        "polarity_index": 1.0
      }, 
      {
        "-1": 0.0, 
        "0": 0.5, 
        "1": 0.5, 
        "date": "Sun, 22 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.2
      }
    ], 
    "name": "#sundayvibes", 
    "promoted_content": null, 
    "query": "%23sundayvibes", 
    "show": false, 
    "tweet_volume": 18124, 
    "url": "http://twitter.com/search?q=%23sundayvibes"
  }, 
  {
    "date_polarity_counts": [
      {
        "-1": 0.3, 
        "0": 0.2, 
        "1": 0.5, 
        "date": "Sun, 22 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.7142857142857143
      }
    ], 
    "name": "#CatturdsFartingArmy", 
    "promoted_content": null, 
    "query": "%23CatturdsFartingArmy", 
    "show": false, 
    "tweet_volume": 10245, 
    "url": "http://twitter.com/search?q=%23CatturdsFartingArmy"
  }, 
  {
    "date_polarity_counts": [
      {
        "-1": 0.0, 
        "0": 1.0, 
        "1": 0.0, 
        "date": "Tue, 17 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Sat, 21 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.16666666666666666
      }, 
      {
        "-1": 0.1, 
        "0": 0.1, 
        "1": 0.8, 
        "date": "Sun, 22 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.10204081632653064
      }
    ], 
    "name": "#SundayMorning", 
    "promoted_content": null, 
    "query": "%23SundayMorning", 
    "show": false, 
    "tweet_volume": 14299, 
    "url": "http://twitter.com/search?q=%23SundayMorning"
  }, 
  {
    "date_polarity_counts": [
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Mon, 16 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.24999999999999994
      }, 
      {
        "-1": 0.3333333333333333, 
        "0": 0.0, 
        "1": 0.6666666666666666, 
        "date": "Tue, 17 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.5
      }, 
      {
        "-1": 0.0, 
        "0": 0.75, 
        "1": 0.25, 
        "date": "Wed, 18 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.28571428571428564
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Fri, 20 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.3333333333333333, 
        "0": 0.3333333333333333, 
        "1": 0.3333333333333333, 
        "date": "Sat, 21 Nov 2020 00:00:00 GMT", 
        "polarity_index": Infinity
      }, 
      {
        "-1": 0.1, 
        "0": 0.5, 
        "1": 0.4, 
        "date": "Sun, 22 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.3846153846153846
      }
    ], 
    "name": "#BestBuy", 
    "promoted_content": null, 
    "query": "%23BestBuy", 
    "show": false, 
    "tweet_volume": null, 
    "url": "http://twitter.com/search?q=%23BestBuy"
  }, 
  {
    "date_polarity_counts": [
      {
        "-1": 0.0, 
        "0": 0.7, 
        "1": 0.3, 
        "date": "Mon, 16 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.13513513513513517
      }, 
      {
        "-1": 0.1, 
        "0": 0.9, 
        "1": 0.0, 
        "date": "Tue, 17 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.06849315068493152
      }, 
      {
        "-1": 0.1, 
        "0": 0.8, 
        "1": 0.1, 
        "date": "Wed, 18 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.10204081632653064
      }, 
      {
        "-1": 0.1, 
        "0": 0.8, 
        "1": 0.1, 
        "date": "Thu, 19 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.10204081632653064
      }, 
      {
        "-1": 0.0, 
        "0": 0.7, 
        "1": 0.3, 
        "date": "Fri, 20 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.13513513513513517
      }, 
      {
        "-1": 0.1, 
        "0": 0.8, 
        "1": 0.1, 
        "date": "Sat, 21 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.10204081632653064
      }, 
      {
        "-1": 0.7, 
        "0": 0.1, 
        "1": 0.2, 
        "date": "Sun, 22 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.16129032258064518
      }
    ], 
    "name": "Huntington Beach", 
    "promoted_content": null, 
    "query": "%22Huntington+Beach%22", 
    "show": false, 
    "tweet_volume": 13074, 
    "url": "http://twitter.com/search?q=%22Huntington+Beach%22"
  }, 
  {
    "date_polarity_counts": [
      {
        "-1": 0.0, 
        "0": 0.6666666666666666, 
        "1": 0.3333333333333333, 
        "date": "Sun, 22 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.5
      }
    ], 
    "name": "#FULEVE", 
    "promoted_content": null, 
    "query": "%23FULEVE", 
    "show": false, 
    "tweet_volume": null, 
    "url": "http://twitter.com/search?q=%23FULEVE"
  }, 
  {
    "date_polarity_counts": [
      {
        "-1": 0.0, 
        "0": 0.16666666666666666, 
        "1": 0.8333333333333334, 
        "date": "Mon, 16 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.14285714285714285
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Tue, 17 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.16666666666666666
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Thu, 19 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Fri, 20 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Sun, 22 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.05000000000000001
      }
    ], 
    "name": "Good Sunday", 
    "promoted_content": null, 
    "query": "%22Good+Sunday%22", 
    "show": false, 
    "tweet_volume": 36276, 
    "url": "http://twitter.com/search?q=%22Good+Sunday%22"
  }, 
  {
    "date_polarity_counts": [
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Mon, 16 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.24999999999999994
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Tue, 17 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Wed, 18 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Sat, 21 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Sun, 22 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }
    ], 
    "name": "John Cleese", 
    "promoted_content": null, 
    "query": "%22John+Cleese%22", 
    "show": false, 
    "tweet_volume": null, 
    "url": "http://twitter.com/search?q=%22John+Cleese%22"
  }, 
  {
    "date_polarity_counts": [
      {
        "-1": 1.0, 
        "0": 0.0, 
        "1": 0.0, 
        "date": "Mon, 16 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.0, 
        "0": 0.5, 
        "1": 0.5, 
        "date": "Tue, 17 Nov 2020 00:00:00 GMT", 
        "polarity_index": 1.0
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Wed, 18 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.0, 
        "0": 0.0, 
        "1": 1.0, 
        "date": "Thu, 19 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.0, 
        "0": 1.0, 
        "1": 0.0, 
        "date": "Fri, 20 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }, 
      {
        "-1": 0.2, 
        "0": 0.3, 
        "1": 0.5, 
        "date": "Sun, 22 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.7142857142857142
      }
    ], 
    "name": "Fulham", 
    "promoted_content": null, 
    "query": "Fulham", 
    "show": false, 
    "tweet_volume": 14318, 
    "url": "http://twitter.com/search?q=Fulham"
  }, 
  {
    "date_polarity_counts": [
      {
        "-1": 0.5, 
        "0": 0.0, 
        "1": 0.5, 
        "date": "Tue, 17 Nov 2020 00:00:00 GMT", 
        "polarity_index": 1.0
      }, 
      {
        "-1": 1.0, 
        "0": 0.0, 
        "1": 0.0, 
        "date": "Sun, 22 Nov 2020 00:00:00 GMT", 
        "polarity_index": 0.4999999999999999
      }
    ], 
    "name": "Iwobi", 
    "promoted_content": null, 
    "query": "Iwobi", 
    "show": false, 
    "tweet_volume": null, 
    "url": "http://twitter.com/search?q=Iwobi"
  }
],
		chartdata: [],
		chartdataBar: [],
		chartdataBar_search: [],
		chartdata_search: [],
		options: {
			responsive: true,
			maintainAspectRatio: false,
			aspectRaio: 2,
			scales: {
				xAxes: [{
					display: true,
					gridLines: {
						display: false
					},
					scaleLabel: {
						display: true,
						labelString: 'Day'
					}
				}],
				yAxes: [{
					display: true,
					gridLines: {
						display: true,
						color: 'white'
					},
					scaleLabel: {
						display: true
					}
				}]
			}
		},
		optionsBar: {
			responsive: true,
			maintainAspectRatio: false,
			aspectRaio: 2,
			title: {
				display: true,
				text: 'Sentiment Trend this week'
			},
			scales: {
				xAxes: [{
					display: true,
					gridLines: {
						display: false
					},
					scaleLabel: {
						display: true,
						labelString: 'Day'
					}
				}],
				yAxes: [{
					display: true,
					gridLines: {
						display: true,
						color: 'white'
					},
					scaleLabel: {
						display: true
					}
				}]
			}
		}
	}
  },
created(){
	let hashtags = this.hashtags;
	this.fetch(hashtags);
},
methods:{
	goto: function(link){
		window.location.href=link;
	},
	fetch_search: function(hashtag){
		console.log(hashtag);
		let pos = [], neg = [], neutral = [], chartdataBar = [], label = [], chartdata = [], score = [];
		for(let iter of hashtag['date_polarity_counts']){
				if("1" in iter)
					pos.push(iter["1"]);
				else
					pos.push(0);
				if("-1" in iter)
					neg.push(iter["-1"]);
				else
					neg.push(0);
				if("0" in iter)
					neutral.push(iter["0"]);
				else
					neutral.push(0);
				label.push(iter["date"].substring(0,3));
				score.push(iter["polarity_index"]);
				// console.log(iter);
			}
			chartdataBar.push(
				{
				labels: label,
				datasets: [
					{
						backgroundColor: 'blue',
						borderColor: 'blue',
						data: pos,
						label: 'Positive',
						fill: false,
					},
					{
						backgroundColor: 'red',
						borderColor: 'red',
						data: neg,
						label: 'Negative',
						fill: false
					},
					{
						backgroundColor: 'yellow',
						borderColor: 'yellow',
						data: neutral,
						label: 'Neutral',
						fill: false
					}
				]
				}
			);
			chartdata.push(
				{
					labels: label,
					datasets: [
					{
						backgroundColor: 'blue',
						borderColor: 'blue',
						data: score,
						fill: false,
						label: "Polarity Index"
					}
					]
				}
			)
		this.chartdataBar_search = chartdataBar;
		this.chartdata_search = chartdata;
	},
	search: function(){
		this.search_active = true;
		this.fetch_search(this.hashtag_search);
		// this.$http.get('https://41138d1d5c0a.ngrok.io/polarityByDay', {params: {query: this.search_query}}).then(resp => {
		// 	console.log("success");
		// 	this.hashtag_search = resp.body;
		// 	this.search_active = true;
		// }, resp => {
		// 	alert("An error occured");
		// 	console.log("error");
		// 	console.log(resp)
		// });
	},
	fetch: function(hashtags){
		let pos = [], neg = [], neutral = [], hashtag, chartdataBar = [], label = [], chartdata = [], score = [];
		for(hashtag of hashtags){
			pos = [];
			neg = [];
			neutral = [];
			label = [];
			score = [];
			for(let iter of hashtag['date_polarity_counts']){
				if("1" in iter)
					pos.push(iter["1"]);
				else
					pos.push(0);
				if("-1" in iter)
					neg.push(iter["-1"]);
				else
					neg.push(0);
				if("0" in iter)
					neutral.push(iter["0"]);
				else
					neutral.push(0);
				label.push(iter["date"].substring(0,3));
				if(iter["polarity_index"] !== Infinity)
					score.push(iter["polarity_index"]);
				else
					score.push(10);
				// console.log(iter);
			}
			chartdataBar.push(
				{
				labels: label,
				datasets: [
					{
						backgroundColor: 'blue',
						borderColor: 'blue',
						data: pos,
						label: 'Positive',
						fill: false,
					},
					{
						backgroundColor: 'red',
						borderColor: 'red',
						data: neg,
						label: 'Negative',
						fill: false
					},
					{
						backgroundColor: 'yellow',
						borderColor: 'yellow',
						data: neutral,
						label: 'Neutral',
						fill: false
					}
				]
				}
			);
			chartdata.push(
				{
					labels: label,
					datasets: [
					{
						backgroundColor: 'blue',
						borderColor: 'blue',
						data: score,
						fill: false,
						label: "Polarity Index"
					}
					]
				}
			)
		}
		this.chartdataBar = chartdataBar;
		this.chartdata = chartdata;
	}
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  margin-top: 60px;
}
.container-fluid, .navbar {
	background-color: rgb(21, 32, 43);
	padding-block-end: 100px;
	padding-block-start: 10px;
}
.navbar {
	flex-wrap: nowrap !important;
}
.topic {
	
}
.hashtag {
	border: 1px solid black;
	margin: 5px;
}
.hashtag-desc {
	color: rgb(136, 153, 166);
}
.hashtag-card {
	background-color: inherit !important;
	border: 1px solid white !important;
	flex-direction: inherit !important;
	margin-top: 10px;
	margin-bottom: 5px;
}
.form-inline {
	flex-flow: nowrap !important;
}
.small {
	width: 250px;
	height: 150px;
}
.medium {
	width: 550px;
	height: 250px;
}
</style>

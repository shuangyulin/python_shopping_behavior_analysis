<template>
	<div class="home-content">
		<!-- title -->
		<div id="home-title" class="home-title animate__animated">
			<div class="titles" >
				{{this.$project.projectName}}
			</div>
		</div>
		<div id="user-box" class="user-box animate__animated">
			<div class="user-top-box">
				<el-image class="avatar" :src="avatar?this.$base.url + avatar : require('@/assets/img/avator.png')"></el-image>
				<div class="user-top-item">
					<div class="nickname">
						<span>用户名</span>
						{{this.$storage.get('adminName')}}
					</div>
					<div class="role">
						<span>角色</span>
						{{this.$storage.get('role')}}
					</div>
				</div>
			</div>
			<div class="user-bottom-box">
				<div class="ip">
					<span>上次登录地址：</span>
					<span>{{locationIp?locationIp:'首次登录'}}</span>
				</div>
				<div class="time">
					<span>上次登录时间：</span>
					<span>{{locationTime?locationTime:'首次登录'}}</span>
				</div>
			</div>
		</div>
		<!-- statis -->
		<div class="statis-box">
			<div id="statis1" class="statis1 animate__animated" v-if="isAuth('yonghu','首页总数')">
				<div class="left">
					<span class="icon iconfont icon-tongji5"></span>
				</div>
				<div class="right">
					<div class="num">{{yonghuCount}}</div>
					<div class="name">用户总数</div>
				</div>
			</div>
			<div id="statis2" class="statis2 animate__animated" v-if="isAuth('shangpinxinxi','首页总数')">
				<div class="left">
					<span class="icon iconfont icon-tongjitu01"></span>
				</div>
				<div class="right">
					<div class="num">{{shangpinxinxiCount}}</div>
					<div class="name">商品信息总数</div>
				</div>
			</div>
			<div id="statis3" class="statis3 animate__animated" v-if="isAuth('gouwurizhi','首页总数')">
				<div class="left">
					<span class="icon iconfont icon-tongji7"></span>
				</div>
				<div class="right">
					<div class="num">{{gouwurizhiCount}}</div>
					<div class="name">购物日志总数</div>
				</div>
			</div>
		</div>
		<!-- statis -->
		<div id="news-box" class="news-box animate__animated">
			<div class="news-title">
				公告资讯
			</div>
			<div class="news-list">
				<div class="news-item" v-for="(item,index) in newsList" :index="index" @click="newsDetailClick(item)">
					<div class="news-text">
						{{item.title}}
					</div>
					<div class="news-time">
						{{item.addtime}}
					</div>
				</div>
			</div>
		</div>
		<el-dialog :visible.sync="newsVisible" title="公告资讯" :append-to-body="true" width="60%">
			<div style="width: 100%;text-align: center;font-size: 20px;color: #000;padding: 0 0 20px;font-weight: bold;">{{newsDetail.title}}</div>
			<div style="width: 100%;">
				<div v-html="newsDetail.content"></div>
			</div>
		</el-dialog>
	
		<!-- echarts -->
		<!-- 5 -->
		<div class="type5">
			<div id="yonghuChart1" class="echarts1 animate__animated" v-if="isAuth('yonghu','首页统计')"></div>
			<div id="shangpinxinxiChart1" class="echarts2 animate__animated" v-if="isAuth('shangpinxinxi','首页统计')"></div>
			<div id="shangpinxinxiChart2" class="echarts3 animate__animated" v-if="isAuth('shangpinxinxi','首页统计')"></div>
			<div id="shangpinxinxiChart3" class="echarts4 animate__animated" v-if="isAuth('shangpinxinxi','首页统计')"></div>
			<div id="shangpinxinxiChart4" class="echarts5 animate__animated" v-if="isAuth('shangpinxinxi','首页统计')"></div>
		</div>
	</div>
</template>
<script>
import 'animate.css'
//5
import router from '@/router/router-static'
import * as echarts from 'echarts'
export default {
	data() {
		return {
			yonghuCount: 0,
			shangpinxinxiCount: 0,
			gouwurizhiCount: 0,
			line: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#5470c6","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"#333","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"showSymbol":true,"symbol":"emptyCircle","symbolSize":4},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"}},
			bar: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":12,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#333","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#333","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#00ff00","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"#333","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"barWidth":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"colorBy":"data","barCategoryGap":"20%"},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"},"base":{"animate":false,"interval":2000}},
			pie: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#5470c6","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"title":{"borderType":"solid","padding":[5,0,0,0],"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#333","textShadowColor":"transparent","fontSize":14,"lineHeight":14,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":[5,0,0,0],"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":2,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":0,"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":2,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#666","color":"inherit","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#666","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false}}},
			funnel: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#5470c6","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"title":{"borderType":"solid","padding":2,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"center","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#666","textShadowColor":"transparent","fontSize":14,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#ccc","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":5,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":2,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":2,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false}}},
			boardBase: {"funnelNum":8,"lineNum":8,"gaugeNum":8,"barNum":8,"pieNum":8},
			gauge: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#5470c6","#91cc75","#fac858","#ee6666","#73c0de","#3ba272","#fc8452","#9a60b4","#ea7ccc"],"title":{"top":"top","left":"left","textStyle":{"fontSize":14,"lineHeight":24,"color":"#333","fontWeight":600}},"series":{"pointer":{"offsetCenter":[0,"10%"],"icon":"path://M2.9,0.7L2.9,0.7c1.4,0,2.6,1.2,2.6,2.6v115c0,1.4-1.2,2.6-2.6,2.6l0,0c-1.4,0-2.6-1.2-2.6-2.6V3.3C0.3,1.9,1.4,0.7,2.9,0.7z","width":8,"length":"80%"},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"opacity":0.5,"shadowBlur":1,"shadowColor":"#000"},"roundCap":true},"anchor":{"show":true,"itemStyle":{"color":"inherit"},"size":18,"showAbove":true},"emphasis":{"disabled":false},"progress":{"show":true,"roundCap":true,"overlap":true},"splitNumber":25,"detail":{"formatter":"{value}","backgroundColor":"inherit","color":"#fff","borderRadius":3,"width":20,"fontSize":12,"height":10},"title":{"fontSize":14},"animation":true}},
			newsList: [],
			newsDetail: {},
			newsVisible: false,
		};
	},
	mounted(){
		this.init();
		this.getyonghuCount();
		if(this.isAuth('yonghu','首页统计')){
			this.yonghuChat1();
		}
		this.getshangpinxinxiCount();
		if(this.isAuth('shangpinxinxi','首页统计')){
			this.shangpinxinxiChat1();
		}
		if(this.isAuth('shangpinxinxi','首页统计')){
			this.shangpinxinxiChat2();
		}
		if(this.isAuth('shangpinxinxi','首页统计')){
			this.shangpinxinxiChat3();
		}
		if(this.isAuth('shangpinxinxi','首页统计')){
			this.shangpinxinxiChat4();
		}
		this.getgouwurizhiCount();
		window.addEventListener('scroll', this.handleScroll)
		setTimeout(()=>{
			this.handleScroll()
		},100)
	},
	computed: {
		avatar(){
			return this.$storage.get('headportrait')?this.$storage.get('headportrait'):''
		},
		locationIp(){
			return this.$storage.get('beforeLocation')?this.$storage.get('beforeLocation'):''
		},
		locationTime(){
			return this.$storage.get('beforeTime')?this.$storage.get('beforeTime'):''
		},
	},
	methods:{
		handleScroll() {
			let arr = [
				{id:'home-title',css:'animate__fadeInUp'},
				{id:'user-box',css:'animate__fadeInUp'},
				{id:'statis1',css:'animate__fadeInUp'},
				{id:'statis2',css:'animate__fadeInUp'},
				{id:'statis3',css:'animate__fadeInUp'},
				{id:'news-box',css:'animate__fadeInUp'},
				{id:'yonghuChart1',css:'animate__bounce'},
				{id:'shangpinxinxiChart1',css:'animate__bounce'},
				{id:'shangpinxinxiChart2',css:'animate__bounce'},
				{id:'shangpinxinxiChart3',css:'animate__bounce'},
				{id:'shangpinxinxiChart4',css:'animate__bounce'},
			]
			
			for (let i in arr) {
				let doc = document.getElementById(arr[i].id)
				if (doc) {
					let top = doc.offsetTop
					let win_top = window.innerHeight + window.pageYOffset
					// console.log(top,win_top)
					if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
						// console.log(doc)
						doc.classList.add(arr[i].css)
					}
				}
			}
		},
		// 统计图动画
		myChartInterval(type, xAxisData, seriesData, myChart) {
			this.$nextTick(() => {
				setInterval(() => {
					let xAxis = xAxisData.shift()
					xAxisData.push(xAxis)
					let series = seriesData.shift()
					seriesData.push(series)
				
					if (type == 1) {
						myChart.setOption({
							xAxis: [{
								data: xAxisData
							}],
							series: [{
								data: seriesData
							}]
						});
					}
					if (type == 2) {
						myChart.setOption({
							yAxis: [{
								data: xAxisData
							}],
							series: [{
								data: seriesData
							}]
						});
					}
				}, $template2.back.board.bar.base.interval);
			})
		},
		init(){
			if(this.$storage.get('Token')){
				this.$http({
					url: `${this.$storage.get('sessionTable')}/session`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code != 0) {
						router.push({ name: 'login' })
					}
				});
			}else{
				router.push({ name: 'login' })
			}
			this.getNewsList()
		},
		getNewsList(){
			let params = {
				page: 1,
				limit: 6,
				sort: 'addtime',
				order: 'desc',
			}
			this.$http({
				url: `news/list`,
				method: "get",
				params: params
			}).then(res => {
				if(res.data&&res.data.code==0){
					this.newsList = res.data.data.list
				}
			});
		},
		newsDetailClick(row){
			this.newsDetail = row
			this.newsVisible = true
		},
		getyonghuCount() {
			this.$http({
				url: `yonghu/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.yonghuCount = data.data
				}
			})
		},
// 1234 饼
		yonghuChat1() {
			this.$nextTick(()=>{

				var yonghuChart1 = echarts.init(document.getElementById("yonghuChart1"),'macarons');
				this.$http({
					url: "yonghu/sectionStat/nianling",
					method: "get",
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.pieNum){
								break;
							}
							xAxis.push(res[i].nianling);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].nianling
							})
						}
						var option = {};
						let titleObj = this.pie.title
						titleObj.text = '年龄统计'
						
						const legendObj = this.pie.legend
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c} ({d}%)'}
						tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
						
						let seriesObj = {
							type: 'pie',
							radius: '55%',
							center: ['50%', '60%'],
							data: pArray,
							emphasis: {
								itemStyle: {
									shadowBlur: 10,
									shadowOffsetX: 0,
									shadowColor: 'rgba(0, 0, 0, 0.5)'
								}
							}
						}
						seriesObj = Object.assign(seriesObj , this.pie.series)
						const gridObj = this.pie.grid
						option = {
							backgroundColor: this.pie.backgroundColor,
							color: this.pie.color,
							title: titleObj,
							legend: legendObj,
							grid: gridObj,
							tooltip: tooltipObj,
							series: [seriesObj]
						};
						// 使用刚指定的配置项和数据显示图表。
						yonghuChart1.setOption(option);
				
						//根据窗口的大小变动图表
						window.addEventListener('resize', () => {
							yonghuChart1.resize()
						})
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},


		getshangpinxinxiCount() {
			this.$http({
				url: `shangpinxinxi/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.shangpinxinxiCount = data.data
				}
			})
		},
// 1234 仪
		shangpinxinxiChat1() {
			this.$nextTick(()=>{

				var shangpinxinxiChart1 = echarts.init(document.getElementById("shangpinxinxiChart1"),'macarons');
				this.$http({
					url: "shangpinxinxi/group/shangpinleixing",
					method: "get",
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						if(this.boardBase&&this.boardBase.gaugeNum>6){
							this.boardBase.gaugeNum = 6
						}
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.gaugeNum){
								break;
							}
							xAxis.push(res[i].shangpinleixing);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].shangpinleixing
							})
						}
						var option = {};
						let titleObj = this.gauge.title
						titleObj.text = '商品类型'
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.gauge.tooltip?this.gauge.tooltip:{})
						
						for(let x=0;x<pArray.length;x++){
							pArray[x] = Object.assign(pArray[x], {
								title: {
									offsetCenter: [String((-200 + (x) * 80) + '%'), '80%']
								},
								detail: {
									offsetCenter: [String((-200 + (x) * 80) + '%'), '105%']
								}
							})
						}
						let seriesObj = {
							data: pArray,
							type: 'gauge',
						}
						seriesObj = Object.assign(seriesObj, this.gauge.series)
						const gridObj = this.gauge.grid
						option = {
							backgroundColor: this.gauge.backgroundColor,
							color: this.gauge.color,
							title: titleObj,
							tooltip: tooltipObj,
							series: [seriesObj],
							grid: gridObj
						}
						// 使用刚指定的配置项和数据显示图表。
						shangpinxinxiChart1.setOption(option);
				
						//根据窗口的大小变动图表
						window.addEventListener('resize', () => {
							shangpinxinxiChart1.resize()
						})
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},

		shangpinxinxiChat2() {
			this.$nextTick(()=>{

				var shangpinxinxiChart2 = echarts.init(document.getElementById("shangpinxinxiChart2"),'macarons');
				this.$http({
					url: `shangpinxinxi/value/shangpinleixing/thumbsupnum`,
					method: "get",
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.barNum){
								break;
							}
							xAxis.push(res[i].shangpinleixing);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].shangpinleixing
							})
						}
						var option = {};
						let titleObj = this.bar.title
						titleObj.text = '点赞统计'
						
						const legendObj = this.bar.legend
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.bar.tooltip?this.bar.tooltip:{})
				
						let xAxisObj = this.bar.xAxis
						xAxisObj.type = 'category'
						xAxisObj.data = xAxis
						
						let yAxisObj = this.bar.yAxis
						yAxisObj.type = 'value'
						let seriesObj = {
							data: yAxis,
							type: 'bar'
						}
						seriesObj = Object.assign(seriesObj , this.bar.series)
						const gridObj = this.bar.grid

						option = {
							backgroundColor: this.bar.backgroundColor,
							color: this.bar.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							xAxis: xAxisObj,
							yAxis: yAxisObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						shangpinxinxiChart2.setOption(option);
				
						//根据窗口的大小变动图表
						window.addEventListener('resize', () => {
							shangpinxinxiChart2.resize()
						})
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},

		shangpinxinxiChat3() {
			this.$nextTick(()=>{

				var shangpinxinxiChart3 = echarts.init(document.getElementById("shangpinxinxiChart3"),'macarons');
				this.$http({
					url: `shangpinxinxi/value/shangpinleixing/storeupnum`,
					method: "get",
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.lineNum){
								break;
							}
							xAxis.push(res[i].shangpinleixing);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].shangpinleixing
							})
						}
						var option = {};
						let titleObj = this.line.title
						titleObj.text = '收藏统计'
						
						const legendObj = this.line.legend
						let tooltipObj = { trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.line.tooltip?this.line.tooltip:{})
						
						let xAxisObj = this.line.xAxis
						xAxisObj.type = 'category'
						xAxisObj.boundaryGap = false
						xAxisObj.data = xAxis
						
						let yAxisObj = this.line.yAxis
						yAxisObj.type = 'value'
						
						let seriesObj = {
							data: yAxis,
							type: 'line',
						}
						seriesObj = Object.assign(seriesObj , this.line.series)
						const gridObj = this.line.grid
						option = {
							backgroundColor: this.line.backgroundColor,
							color: this.line.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							xAxis: xAxisObj,
							yAxis: yAxisObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						shangpinxinxiChart3.setOption(option);
						//根据窗口的大小变动图表
						window.addEventListener('resize', () => {
							shangpinxinxiChart3.resize()
						})
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},
		shangpinxinxiChat4() {
			this.$nextTick(()=>{

				var shangpinxinxiChart4 = echarts.init(document.getElementById("shangpinxinxiChart4"),'macarons');
				this.$http({
					url: `shangpinxinxi/value/shangpinleixing/discussnum`,
					method: "get",
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data;
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.lineNum){
								break;
							}
							xAxis.push(res[i].shangpinleixing);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].shangpinleixing
							})
						}
						var option = {};
						let titleObj = this.line.title
						titleObj.text = '评论统计'
						
						const legendObj = this.line.legend
						let tooltipObj = { trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.line.tooltip?this.line.tooltip:{})
						
						let xAxisObj = this.line.xAxis
						xAxisObj.type = 'category'
						xAxisObj.boundaryGap = false
						xAxisObj.data = xAxis
						
						let yAxisObj = this.line.yAxis
						yAxisObj.type = 'value'
						
						let seriesObj = {
							data: yAxis,
							type: 'line',
							areaStyle: {}
						}
						seriesObj = Object.assign(seriesObj , this.line.series)
						const gridObj = this.line.grid
						option = {
							backgroundColor: this.line.backgroundColor,
							color: this.line.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							xAxis: xAxisObj,
							yAxis: yAxisObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						shangpinxinxiChart4.setOption(option);

						//根据窗口的大小变动图表
						window.addEventListener('resize', () => {
							shangpinxinxiChart4.resize()
						})
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},
		getgouwurizhiCount() {
			this.$http({
				url: `gouwurizhi/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.gouwurizhiCount = data.data
				}
			})
		},
// 1234 横


	}
};
</script>
<style lang="scss" scoped>
	.home-content {
		padding: 30px;
		display: flex;
		justify-content: flex-start;
		flex-wrap: wrap;
		.home-title {
			border-radius: 5px;
			padding: 10px 0;
			box-shadow: 0 0px 0px rgba(0,0,0,.3);
			margin: 10px 0;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: center;
			transition: 0.3s;
			.titles {
				padding: 0 0 0 12px;
				color: #333;
				font-size: 24px;
				line-height: 44px;
			}
		}
		.home-title:hover {
			transform: translate3d(0, 0px, 0);
			z-index: 1;
			background: rgba(255,255,255,.12);
		}
		.user-box {
			border: 1px solid #ccc;
			border-radius: 2px;
			padding: 10px 20px;
			box-shadow: 0 0px 0px rgba(0,0,0,.3);
			margin: 10px;
			flex-direction: column;
			display: block;
			width: calc(30% - 20px);
			justify-content: center;
			align-items: center;
			transition: 0.3s;
			.user-top-box {
				padding: 0 0 10px;
				margin: 0 0 10px;
				display: flex;
				border-color: #ccc;
				border-width:  0 0 1px;
				align-items: center;
				border-style: solid;
				.avatar {
					border-radius: 100%;
					object-fit: cover;
					width: 60px;
					height: 60px;
				}
				.user-top-item {
					width: 100%;
					.nickname {
						padding: 0;
						color: #666;
						font-size: 14px;
						line-height: 1.5;
						span {
							padding: 0;
							margin: 0 10px;
							color: #000;
							font-size: 14px;
							line-height: 1.5;
						}
					}
					.role {
						padding: 0;
						color: #666;
						font-size: 14px;
						line-height: 1.5;
						span {
							padding: 0;
							margin: 0 10px;
							color: #000;
							font-size: 14px;
							line-height: 1.5;
						}
					}
				}
			}
			.user-bottom-box {
				flex-direction: column;
				display: flex;
				line-height: 2;
				align-items: flex-start;
				.ip {
					display: flex;
					justify-content: center;
					span:nth-child(1) {
						color: #999;
					}
					span:nth-child(2) {
						color: #444;
					}
				}
				.time {
					display: flex;
					justify-content: center;
					span:nth-child(1) {
						color: #999;
					}
					span:nth-child(2) {
						color: #444;
					}
				}
			}
		}
		.user-box:hover {
			box-shadow: 0 1px 6px rgba(0,0,0,.1);
			transform: translate3d(0, -10px, 0);
		}
		.statis-box {
			padding: 0;
			margin: 10px;
			display: flex;
			width: calc(70% - 20px);
			justify-content: flex-start;
			align-items: center;
			.statis1 {
				border: 1px solid #ccc;
				border-radius: 2px;
				margin: 0 10px 10px;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: #f1bc41;
					display: flex;
					width: 80px;
					justify-content: center;
					align-items: center;
					height: 80px;
					.iconfont {
						color: #fff;
						font-size: 24px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 160px;
					justify-content: center;
					align-items: center;
					.num {
						margin: 5px 0;
						color: #333;
						font-weight: bold;
						font-size: 20px;
						line-height: 24px;
						height: 24px;
					}
					.name {
						margin: 5px 0;
						color: #666;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis1:hover {
				transform: translate3d(0, -10px, 0);
				z-index: 1;
				background: rgba(255,255,255,.12);
			}
			.statis2 {
				border: 1px solid #ccc;
				border-radius: 2px;
				box-shadow: 0 0x 0px rgba(0,0,0,.3);
				margin: 0 10px 10px;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: #f44680;
					display: flex;
					width: 80px;
					justify-content: center;
					align-items: center;
					height: 80px;
					.iconfont {
						color: #fff;
						font-size: 24px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 160px;
					justify-content: center;
					align-items: center;
					.num {
						margin: 5px 0;
						color: #333;
						font-weight: bold;
						font-size: 20px;
						line-height: 24px;
						height: 24px;
					}
					.name {
						margin: 5px 0;
						color: #666;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis2:hover {
				transform: translate3d(0, -10px, 0);
				z-index: 1;
				background: rgba(255,255,255,.12);
			}
			.statis3 {
				border: 1px solid #ccc;
				border-radius: 2px;
				box-shadow: 0 0px 0px rgba(0,0,0,.3);
				margin: 0 10px 10px;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: #9582d7;
					display: flex;
					width: 80px;
					justify-content: center;
					align-items: center;
					height: 80px;
					.iconfont {
						color: #fff;
						font-size: 24px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 160px;
					justify-content: center;
					align-items: center;
					.num {
						margin: 5px 0;
						color: #333;
						font-weight: bold;
						font-size: 20px;
						line-height: 24px;
						height: 24px;
					}
					.name {
						margin: 5px 0;
						color: #666;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis3:hover {
				transform: translate3d(0, -10px, 0);
				z-index: 1;
				background: rgba(255,255,255,.12);
			}
			.statis4 {
				border: 1px solid #ccc;
				border-radius: 2px;
				box-shadow: 0 0px 0px rgba(0,0,0,.3);
				margin: 0 10px 10px;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: #5caa5f;
					display: flex;
					width: 80px;
					justify-content: center;
					align-items: center;
					height: 80px;
					.iconfont {
						color: #fff;
						font-size: 24px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 160px;
					justify-content: center;
					align-items: center;
					.num {
						margin: 5px 0;
						color: #333;
						font-weight: bold;
						font-size: 20px;
						line-height: 24px;
						height: 24px;
					}
					.name {
						margin: 5px 0;
						color: #666;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis4:hover {
				transform: translate3d(0, -10px, 0);
				z-index: 1;
				background: rgba(255,255,255,.12);
			}
			.statis5 {
				border: 1px solid #ccc;
				border-radius: 2px;
				box-shadow: 0 0px 0px rgba(0,0,0,.3);
				margin: 0 10px 10px;
				display: flex;
				width: calc(20% - 20px);
				transition: 0.3s;
				.left {
					background: #5ca5aa;
					display: flex;
					width: 80px;
					justify-content: center;
					align-items: center;
					height: 80px;
					.iconfont {
						color: #fff;
						font-size: 24px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 160px;
					justify-content: center;
					align-items: center;
					.num {
						margin: 5px 0;
						color: #333;
						font-weight: bold;
						font-size: 20px;
						line-height: 24px;
						height: 24px;
					}
					.name {
						margin: 5px 0;
						color: #666;
						font-size: 16px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis5:hover {
				transform: translate3d(0, -10px, 0);
				z-index: 1;
				background: rgba(255,255,255,.12);
			}
		}
		.news-box {
			border: 1px solid #ccc;
			border-radius: 2px;
			padding: 30px;
			box-shadow: 0 0px 0px rgba(0,0,0,.3);
			margin: 10px;
			flex-direction: column;
			display: flex;
			width: calc(30% - 20px);
			justify-content: center;
			align-items: center;
			transition: 0.3s;
			.news-title {
				padding: 0 2px;
				margin: 0 0 20px;
				color: #000;
				font-weight: 600;
				font-size: 20px;
				border-color: #999;
				border-width: 0 0 2px;
				line-height: 44px;
				border-style: solid;
			}
			.news-list {
				flex-direction: column;
				display: flex;
				width: 100%;
				justify-content: space-between;
				align-items: center;
			}
			.news-item {
				border: 1px solid #99999950;
				padding: 10px 0;
				display: flex;
				width: 100%;
				border-width: 0 0 1px;
				justify-content: space-between;
				align-items: center;
				.news-text {
					color: #000;
					font-weight: 500;
					font-size: 14px;
				}
				.news-time {
					color: #666;
					font-size: 12px;
				}
			}
		}
		.news-box:hover {
			box-shadow: 0 1px 6px rgba(0,0,0,.1);
			transform: translate3d(0, -10px, 0);
		}
		// echarts5
		.type5 {
			padding: 0;
			margin: 10px 0;
			align-content: flex-start;
			background: none;
			display: flex;
			width: 100%;
			justify-content: space-between;
			flex-wrap: wrap;
			height: auto;
			.echarts1 {
				border: 1px solid #ccc;
				border-radius: 0px;
				padding: 20px;
				margin: 10px;
				background: rgba(255,255,255,.1);
				width: 100%;
				transition: 0.3s;
				height: 400px;
			}
			.echarts1:hover {
				transform: translate3d(0, -10px, 0);
				z-index: 1;
				background: rgba(255,255,255,.12);
			}
			.echarts2 {
				border: 1px solid #ccc;
				border-radius: 0px;
				padding: 20px;
				margin: 10px;
				background: rgba(255,255,255,.1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts2:hover {
				transform: translate3d(0, -10px, 0);
				z-index: 1;
				background: rgba(255,255,255,.12);
			}
			.echarts3 {
				border: 1px solid #ccc;
				border-radius: 0px;
				padding: 20px;
				margin: 10px;
				background: rgba(255,255,255,.1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts3:hover {
				transform: translate3d(0, -10px, 0);
				z-index: 1;
				background: rgba(255,255,255,.12);
			}
			.echarts4 {
				border: 1px solid #ccc;
				border-radius: 0px;
				padding: 20px;
				margin: 10px;
				background: rgba(255,255,255,.1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts4:hover {
				transform: translate3d(0, -10px, 0);
				z-index: 1;
				background: rgba(255,255,255,.12);
			}
			.echarts5 {
				border: 1px solid #ccc;
				border-radius: 0px;
				padding: 20px;
				margin: 10px;
				background: rgba(255,255,255,.1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 400px;
			}
			.echarts5:hover {
				transform: translate3d(0, -10px, 0);
				z-index: 1;
				background: rgba(255,255,255,.12);
			}
		}
	}
	
	.echarts-flag-2 {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		padding: 10px 20px;
		background: rebeccapurple;
	
		&>div {
			width: 32%;
			height: 300px;
			margin: 10px 0;
			background: rgba(255,255,255,.1);
			border-radius: 8px;
			padding: 10px 20px;
		}
	}
	.animate__animated {
		animation-fill-mode: none;
	}
</style>

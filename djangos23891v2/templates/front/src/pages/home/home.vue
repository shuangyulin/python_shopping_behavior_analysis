<template>
	<div class="home-preview">




		<!-- 系统简介 -->
		<div id="system" class="animate__animated">
			<div class="system_item">
				<div class="system_title_box">
					<div class="system_title">{{systemIntroductionDetail.title}}</div>
					<div class="system_subtitle">{{systemIntroductionDetail.subtitle}}</div>
				</div>
				<div class="system_img">
					<img :src="baseUrl + systemIntroductionDetail.picture1">
					<img :src="baseUrl + systemIntroductionDetail.picture2">
					<img :src="baseUrl + systemIntroductionDetail.picture3">
				</div>
				<div class="system_content" v-html="systemIntroductionDetail.content"></div>
				<div class="system_idea1" />
				<div class="system_idea2" />
				<div class="system_idea3" />
				<div class="system_idea4" />
				<div class="system_more" @click="toDetail('systemintroDetail',systemIntroductionDetail)">
					<span>查看更多</span>
					<span class="icon iconfont icon-gengduo1"></span>
				</div>
			</div>
		</div>
		<!-- 系统简介 -->
		<!-- 新闻资讯 -->
		<div id="animate_newsnews" class="news animate__animated">
			<div class="news_title_box">
				<span class="news_title">公告资讯</span>
				<span class="news_subhead">{{'news'.toUpperCase()}}</span>
			</div>
			<div class="list list25 index-pv1">
				<div class="leftView">
					<div class="titleView">
						<div class="title">公告资讯</div>
						<div class="text">News Information</div>
					</div>
					<div class="list-body">
						<div v-for="(item,index) in newsList" v-if="index<4" :key="index" class="list-item" @click="toDetail('newsDetail', item)">
							<div class="img">
								<img :src="baseUrl + item.picture" alt="">
							</div>
							<div class="infoBox">
								<div class="name">{{item.title}}</div>
								<div class="time">{{item.addtime.split(' ')[0]}}</div>
							</div>
						</div>
					</div>
				</div>
				<div class="rightView">
					<div class="list-item" v-for="(item,index) in newsList" v-if="index>=4&&index<8" :key="index" @click="toDetail('newsDetail', item)">
						<div class="top-info">
							<div class="name">{{item.title}}</div>
							<span class="icon iconfont icon-jiantou25"></span>
						</div>
						<div class="infoBox">
							<img :src="baseUrl + item.picture" alt="">
							<div class="desc">{{item.introduction}}</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('news')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 新闻资讯 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendshangpinxinxi" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">商品信息推荐</span>
				<span class="recommend_subhead">{{'shangpinxinxi'.toUpperCase()}} RECOMMEND</span>
			</div>
			<div class="list list22 index-pv1">
				<div class="list-body-left">
					<div class="list-item1" @click="toDetail('shangpinxinxiDetail', shangpinxinxiRecommend[0])">
						<img v-if="preHttp(shangpinxinxiRecommend[0].shangpintupian)" :src="shangpinxinxiRecommend[0].shangpintupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (shangpinxinxiRecommend[0].shangpintupian?shangpinxinxiRecommend[0].shangpintupian.split(',')[0]:'')" alt="" />
						<div class="name">{{shangpinxinxiRecommend[0].shangpinmingcheng}}</div>
						<div class="name">{{shangpinxinxiRecommend[0].shangpinleixing}}</div>
					</div>
					<div class="list-item2" @click="toDetail('shangpinxinxiDetail', shangpinxinxiRecommend[1])">
						<div class="img">
							<img v-if="preHttp(shangpinxinxiRecommend[1].shangpintupian)" :src="shangpinxinxiRecommend[1].shangpintupian.split(',')[0]" alt="" />
							<img v-else :src="baseUrl + (shangpinxinxiRecommend[1].shangpintupian?shangpinxinxiRecommend[1].shangpintupian.split(',')[0]:'')" alt="" />
						</div>
						<div class="infoBox">
							<div class="name">{{shangpinxinxiRecommend[1].shangpinmingcheng}}</div>
							<div class="name">{{shangpinxinxiRecommend[1].shangpinleixing}}</div>
							<div class="price">￥{{shangpinxinxiRecommend[1].price}}</div>
							<div class="desc">{{shangpinxinxiRecommend[1].shangpinxiangqing}}</div>

							<div class="bottom" >
								<div class="time">{{shangpinxinxiRecommend[1].addtime.split(' ')[0]}}</div>
							</div>
							<div class="jian"></div>
					  </div>
					</div>
				</div>
				<div class="list-body-right">
					<div class="list-item1" @click="toDetail('shangpinxinxiDetail', shangpinxinxiRecommend[2])">
						<div class="img">
							<img v-if="preHttp(shangpinxinxiRecommend[2].shangpintupian)" :src="shangpinxinxiRecommend[2].shangpintupian.split(',')[0]" alt="" />
							<img v-else :src="baseUrl + (shangpinxinxiRecommend[2].shangpintupian?shangpinxinxiRecommend[2].shangpintupian.split(',')[0]:'')" alt="" />
						</div>
						<div class="infoBox">
							<div class="name">{{shangpinxinxiRecommend[2].shangpinmingcheng}}</div>
							<div class="name">{{shangpinxinxiRecommend[2].shangpinleixing}}</div>
							<div class="price">￥{{shangpinxinxiRecommend[2].price}}</div>
							<div class="desc">{{shangpinxinxiRecommend[2].shangpinxiangqing}}</div>

							<div class="bottom">
								<div class="time">{{shangpinxinxiRecommend[2].addtime.split(' ')[0]}}</div>
							</div>
							<div class="jian"></div>
						</div>
					</div>
					<div class="list-item2" @click="toDetail('shangpinxinxiDetail', shangpinxinxiRecommend[3])">
						<div class="infoBox">
							<div class="name">{{shangpinxinxiRecommend[3].shangpinmingcheng}}</div>
							<div class="name">{{shangpinxinxiRecommend[3].shangpinleixing}}</div>
							<div class="price">￥{{shangpinxinxiRecommend[3].price}}</div>
							<div class="desc">{{shangpinxinxiRecommend[3].shangpinxiangqing}}</div>

							<div class="bottom">
								<div class="time">{{shangpinxinxiRecommend[3].addtime.split(' ')[0]}}</div>
							</div>
							<div class="jian"></div>
						</div>
						<div class="img">
							<img v-if="preHttp(shangpinxinxiRecommend[3].shangpintupian)" :src="shangpinxinxiRecommend[3].shangpintupian.split(',')[0]" alt="" />
							<img v-else :src="baseUrl + (shangpinxinxiRecommend[3].shangpintupian?shangpinxinxiRecommend[3].shangpintupian.split(',')[0]:'')" alt="" />
						</div>
					</div>
					<div class="list-item3" @click="toDetail('shangpinxinxiDetail', shangpinxinxiRecommend[4])">
						<div class="img">
							<img v-if="preHttp(shangpinxinxiRecommend[4].shangpintupian)" :src="shangpinxinxiRecommend[4].shangpintupian.split(',')[0]" alt="" />
							<img v-else :src="baseUrl + (shangpinxinxiRecommend[4].shangpintupian?shangpinxinxiRecommend[4].shangpintupian.split(',')[0]:'')" alt="" />
						</div>
						<div class="infoBox">
							<div class="name">{{shangpinxinxiRecommend[4].shangpinmingcheng}}</div>
							<div class="name">{{shangpinxinxiRecommend[4].shangpinleixing}}</div>
							<div class="price">￥{{shangpinxinxiRecommend[4].price}}</div>
							<div class="desc">{{shangpinxinxiRecommend[4].shangpinxiangqing}}</div>

							<div class="bottom">
								<div class="time">{{shangpinxinxiRecommend[4].addtime.split(' ')[0]}}</div>
							</div>
							<div class="jian"></div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('shangpinxinxi')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				systemIntroductionDetail: {},
				newsList: [],
				shangpinxinxiRecommend: [],





			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getNewsList();
			this.getSystemIntroduction();
			this.getList();
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		//方法集合
		methods: {
			swiperChanges() {
				setTimeout(()=>{
				},750)
			},

			listIndexClick23(index, name) {
				this['listIndex23' + name] = index[this['listColumn23' + name]]
				this.getList()
			},

			handleScroll() {
				let arr = [
					{id:'about',css:'animate__'},
					{id:'system',css:'animate__'},
					{id:'animate_recommendshangpinxinxi',css:'animate__'},
					{id:'animate_newsnews',css:'animate__'},
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
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			getSystemIntroduction() {
				this.$http.get('systemintro/detail/1', {}).then(res => {
					if(res.data.code == 0) {
						this.systemIntroductionDetail = res.data.data;
					}
				})
			},
			getNewsList() {
				let data = {
					page: 1,
					limit: 7,
					sort: 'addtime',
					order: 'desc'
				}
				this.$http.get('news/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
					
					}
				});
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
				autoSortUrl = "shangpinxinxi/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "shangpinxinxi/autoSort2";
				}
				data = {
					page: 1,
					limit: 8,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.shangpinxinxiRecommend = res.data.data.list;
					}
				});
			
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		margin: 0px auto;
		flex-direction: column;
		background: #fff;
		display: flex;
		width: 100%;
		#system {
			padding: 20px 0 60px;
			background: #fff;
			width: 100%;
			height: auto;
			order: 5;
			.system_item {
				margin: 0 auto;
				display: block;
				width: 1200px;
				flex-wrap: wrap;
				.system_title_box {
					padding: 0 50px;
					margin: 30px auto 20px;
					background: #03cce9;
					width: 1200px;
					position: relative;
					text-align: left;
					height: 40px;
					.system_title {
						padding: 0 60px;
						margin: -25px 0 0;
						color: #fff;
						background: url(http://codegen.caihongy.cn/20240918/f134e912df3547dd88a98afc1da8b24b.png) no-repeat center top / 100% 100% ;
						display: inline-block;
						width: auto;
						font-size: 22px;
						line-height: 68px;
						height: 64px;
					}
					.system_subtitle {
						color: #999;
						display: none;
						font-size: 24px;
					}
				}
				.system_img {
					padding: 0;
					margin: 20px 0 0;
					background: url(http://codegen.caihongy.cn/20240918/ab2cc4eddbe54b2cad1172abac4bfd5e.png) no-repeat right bottom;
					display: flex;
					width: 720px;
					float: left;
					flex-wrap: wrap;
					height: 450px;
					img:nth-child(1) {
						margin: 0;
						object-fit: cover;
						display: block;
						width: 660px;
						height: 400px;
					}
					img:nth-child(2) {
						object-fit: cover;
						display: none;
						width: 60%;
						height: 100%;
					}
					img:nth-child(3) {
						margin: 0;
						flex: 1;
						object-fit: cover;
						display: none;
						height: 100%;
					}
				}
				.system_content {
					padding: 0;
					margin: 20px 0 10px 0;
					overflow: hidden;
					color: #333;
					background: none;
					width: calc(100% - 750px);
					font-size: 16px;
					line-height: 30px;
					float: right;
					height: 360px;
				}
				.system_idea1 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_idea2 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_idea3 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_idea4 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_more {
					border: 0;
					margin: 10px auto;
					background: #f7db61;
					display: block;
					width: 110px;
					line-height: 32px;
					float: right;
					text-align: center;
					span:nth-child(1) {
						color: #333;
						font-size: 15px;
					}
					span:nth-child(2) {
						color: #333;
						font-size: 15px;
					}
				}
				.system_more:hover {
					cursor: pointer;
					opacity: 1;
				}
			}
		}
		.news {
			padding: 30px 0;
			margin: 20px 0 0;
			background: url(http://codegen.caihongy.cn/20240918/0158f8ec08364ef389a696ea5ad88d08.png) fixed,#018cc030;
			width: 100%;
			position: relative;
			order: 4;
			.news_title_box {
				padding: 0 50px;
				margin: 50px auto 0;
				background: #03cce9;
				width: 1200px;
				position: relative;
				text-align: left;
				height: 40px;
				.news_title {
					padding: 0 60px;
					margin: -24px 0 0;
					color: #fff;
					background: url(http://codegen.caihongy.cn/20240918/f134e912df3547dd88a98afc1da8b24b.png) no-repeat center top / 100% 100% ;
					display: inline-block;
					width: auto;
					font-size: 22px;
					line-height: 68px;
					height: 64px;
				}
				.news_subhead {
					margin: 0 0 10px;
					color: #999;
					display: none;
					width: 100%;
					font-size: 20px;
					line-height: 1.5;
					text-align: center;
				}
			}
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list25 {
				margin: 40px auto;
				display: flex;
				width: 1200px;
				justify-content: space-between;
				align-items: flex-start;
				height: auto;
				.leftView {
					padding: 0px 0 30px;
					background: url(http://codegen.caihongy.cn/20240718/ce12b2c33f0946b2b108e5b99538e42a.jpg) no-repeat center top / 100% 100%;
					width: 370px;
					.titleView {
						padding: 30px 0 10px;
						text-align: center;
						.title {
							color: #333;
							font-weight: 600;
							font-size: 26px;
						}
						.text {
							color: #999;
							font-size: 22px;
						}
					}
					.list-body {
						margin: 0 30px;
						.list-item {
							border: 1px dotted #bababa;
							cursor: pointer;
							padding: 0 0 10px;
							margin: 0 0 20px;
							overflow: hidden;
							display: flex;
							border-width: 0 0 1px;
							height: auto;
							.img {
								margin: 0 16px 0 0;
								overflow: hidden;
								width: 92px;
								height: 75px;
								img {
									object-fit: cover;
									display: block;
									width: 100%;
									transition: all 0.3s ease;
									height: 100%;
								}
							}
							.infoBox {
								display: block;
								.name {
									margin: 0 0 5px;
									overflow: hidden;
									color: #666;
									font-weight: normal;
									display: flex;
									width: 100%;
									font-size: 15px;
									line-height: 24px;
									align-items: center;
									transition: all 0.3s ease;
									height: 48px;
								}
								.time {
									overflow: hidden;
									color: #aaa;
									font-size: 15px;
									transition: all 0.3s ease;
									height: 30px;
								}
							}
						}
						.list-item:hover {
							.img {
								img {
									transform: scale(1.2);
								}
							}
							.infoBox {
								.name {
									color: #000;
								}
								.time {
									color: #c00;
									font-size: 14px;
								}
							}
						}
					}
				}
				.rightView {
					display: flex;
					width: calc(100% - 400px);
					justify-content: space-between;
					flex-wrap: wrap;
					.list-item {
						cursor: pointer;
						width: 48%;
						height: 296px;
						.top-info {
							display: flex;
							width: 100%;
							font-size: 16px;
							line-height: 50px;
							justify-content: space-between;
							align-items: center;
							height: 50px;
							.name {
								color: #333;
								font-size: 16px;
								line-height: 50px;
								height: 50px;
							}
							.icon {
								margin: 0;
								font-size: 16px;
							}
						}
						.infoBox {
							overflow: hidden;
							width: 100%;
							position: relative;
							height: calc(100% - 50px);
							img {
								object-fit: cover;
								display: block;
								width: 100%;
								transition: all 0.3s ease;
								height: 100%;
							}
							.desc {
								padding: 6px 0 0;
								margin: 0 5%;
								color: #666;
								bottom: -30px;
								display: block;
								font-size: 15px;
								line-height: 30px;
								transition: all 0.3s ease;
								overflow: hidden;
								background: rgba(255,255,255,0.7);
								width: 90%;
								position: absolute;
								text-align: center;
								height: 66px;
							}
						}
					}
					.list-item:hover {
						.infoBox {
							img {
								transform: scale(1.2);
							}
							.desc {
								color: #000;
								bottom: 0;
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0;
				cursor: pointer;
				margin: 60px auto;
				top: 0;
				background: #f7db61;
				display: block;
				width: 110px;
				line-height: 32px;
				position: absolute;
				right: calc((100% - 1200px)/2);
				text-align: center;
				.text {
					color: #000;
					font-size: 15px;
				}
				.icon {
					color: #000;
					font-size: 15px;
				}
			}
		}
		.recommend {
			padding: 0;
			margin: 20px 0 0;
			background: #fff;
			width: 100%;
			position: relative;
			.recommend_title_box {
				padding: 0 50px;
				margin: 50px auto 0;
				background: #03cce9;
				width: 1200px;
				text-align: left;
				height: 40px;
				.recommend_title {
					padding: 0 60px;
					margin: -24px 0 0;
					color: #fff;
					background: url(http://codegen.caihongy.cn/20240918/f134e912df3547dd88a98afc1da8b24b.png) no-repeat center top / 100% 100% ;
					display: inline-block;
					width: auto;
					font-size: 22px;
					line-height: 68px;
					height: 64px;
				}
				.recommend_subhead {
					margin: 0 0 10px;
					color: #999;
					display: none;
					width: 100%;
					font-size: 20px;
					line-height: 1.5;
					text-align: center;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, -10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list22 {
				margin: 30px auto 0;
				overflow: hidden;
				display: flex;
				width: 1200px;
				justify-content: space-between;
				.list-body-left {
					width: 49.5%;
					.list-item1 {
						border: 1px solid #eee;
						margin: 0 0 6px;
						overflow: hidden;
						display: block;
						width: 100%;
						position: relative;
						height: 390px;
						img {
							object-fit: cover;
							display: block;
							width: 100%;
							transition: all 0.3s;
							height: 100%;
						}
						.name {
							padding: 0 0 0 20px;
							z-index: 100;
							background-size: 100%;
							color: #fff;
							white-space: nowrap;
							bottom: 0;
							display: block;
							font-size: 15px;
							line-height: 40px;
							text-overflow: ellipsis;
							box-sizing: border-box;
							overflow: hidden;
							left: 0;
							background: rgba(0,0,0,.2);
							width: 100%;
							position: absolute;
							height: 40px;
						}
					}
					.list-item1:hover {
						img {
							cursor: pointer;
							transform: scale(1.05);
						}
						.name {
						}
					}
					.list-item2 {
						cursor: pointer;
						display: flex;
						width: 100%;
						.img {
							border: 1px solid #eee;
							z-index: 50;
							overflow: hidden;
							width: 50%;
							position: relative;
							height: 192px;
							img {
								object-fit: cover;
								display: block;
								width: 100%;
								transition: all 0.3s;
								height: 100%;
							}
						}
						.infoBox {
							padding: 5px 10px 0 10px;
							z-index: 100;
							background: #fcfcfc;
							width: 50%;
							position: relative;
							box-sizing: border-box;
							height: 192px;
							.name {
								padding: 0 10px 0 0;
								margin: 0;
								overflow: hidden;
								color: #404040;
								white-space: nowrap;
								font-weight: 900;
								width: 100%;
								font-size: 15px;
								line-height: 24px;
								text-overflow: ellipsis;
								box-sizing: border-box;
								height: 24px;
							}
							.price {
								margin: 5px 0 0;
								color: #f00;
								font-size: 16px;
							}
							.desc {
								border: 1px dashed #dadada;
								padding: 5px 10px 0 0;
								margin: 5px 0 0;
								overflow: hidden;
								color: #666;
								font-size: 14px;
								border-width: 1px 0 0;
								line-height: 24px;
								box-sizing: border-box;
								height: 48px;
							}
							.bottom {
								margin: 0;
								overflow: hidden;
								background: none;
								bottom: 5px;
								display: flex;
								width: calc(100% - 20px);
								justify-content: space-between;
								position: absolute;
								.publisher {
									color: #747474;
									width: calc(100% - 110px);
									font-size: 14px;
								}
								.time {
									color: #999;
									display: inline;
									width: 110px;
									font-size: 14px;
									line-height: 28px;
									text-align: right;
									height: 28px;
								}
							}
							.jian {
								margin: -7px 0 0;
								clip-path: polygon(100% 1%, 100% 100%, 0% 50%);
								top: 50%;
								left: -8px;
								background: #fcfcfc;
								width: 9px;
								position: absolute;
								height: 14px;
							}
						}
					}
					.list-item2:hover {
						.img {
							img {
								transform: scale(1.05);
							}
						}
						.infoBox {
							background: #03cce9;
							.name {
								color: #fff;
							}
							.price {
								color: #fff;
							}
							.desc {
								color: #fff;
								border-color: #dadada;
							}
							.bottom {
								.publisher {
									color: #fff;
								}
								.time {
									color: #eee;
								}
							}
							.jian {
								background: #03cce9;
							}
						}
					}
				}
				.list-body-right {
					width: 49.5%;
					.list-item1 {
						cursor: pointer;
						margin: 0 0 6px;
						display: flex;
						width: 100%;
						.img {
							border: 1px solid #eee;
							z-index: 50;
							overflow: hidden;
							width: 50%;
							position: relative;
							height: 192px;
							img {
								object-fit: cover;
								display: block;
								width: 100%;
								transition: all 0.3s;
								height: 100%;
							}
						}
						.infoBox {
							padding: 5px 10px 0 10px;
							z-index: 100;
							background: #fcfcfc;
							width: 50%;
							position: relative;
							box-sizing: border-box;
							height: 192px;
							.name {
								padding: 0 10px 0 0;
								margin: 0;
								overflow: hidden;
								color: #404040;
								white-space: nowrap;
								font-weight: 900;
								width: 100%;
								font-size: 15px;
								line-height: 24px;
								text-overflow: ellipsis;
								box-sizing: border-box;
								height: 24px;
							}
							.price {
								margin: 5px 0 0;
								color: #f00;
								font-size: 16px;
							}
							.desc {
								border: 1px dashed #dadada;
								padding: 5px 10px 0 0;
								margin: 5px 0 0;
								overflow: hidden;
								color: #808080;
								font-size: 14px;
								border-width: 1px 0 0;
								line-height: 24px;
								box-sizing: border-box;
								height: 48px;
							}
							.bottom {
								margin: 0;
								overflow: hidden;
								background: none;
								bottom: 5px;
								display: flex;
								width: calc(100% - 20px);
								justify-content: space-between;
								position: absolute;
								.publisher {
									color: #666;
									width: calc(100% - 110px);
									font-size: 14px;
								}
								.time {
									color: #999;
									display: inline;
									width: 110px;
									font-size: 14px;
									line-height: 24px;
									text-align: right;
									height: 24px;
								}
							}
							.jian {
								margin: -7px 0 0;
								clip-path: polygon(100% 1%, 100% 100%, 0% 50%);
								top: 50%;
								left: -8px;
								background: #fcfcfc;
								width: 9px;
								position: absolute;
								height: 14px;
							}
						}
					}
					.list-item1:hover {
						.img {
							img {
								transform: scale(1.05);
							}
						}
						.infoBox {
							background: #03cce9;
							.name {
								color: #fff;
							}
							.price {
								color: #fff;
							}
							.desc {
								color: #fff;
								border-color: #dadada;
							}
							.bottom {
								.publisher {
									color: #fff;
								}
								.time {
									color: #eee;
								}
							}
							.jian {
								background: #03cce9;
							}
						}
					}
					.list-item2 {
						cursor: pointer;
						margin: 0 0 6px;
						display: flex;
						width: 100%;
						.img {
							border: 1px solid #eee;
							z-index: 50;
							overflow: hidden;
							width: 50%;
							position: relative;
							height: 192px;
							img {
								object-fit: cover;
								display: block;
								width: 100%;
								transition: all 0.3s;
								height: 100%;
							}
						}
						.infoBox {
							padding: 5px 10px 0 10px;
							z-index: 100;
							background: #fcfcfc;
							width: 50%;
							position: relative;
							box-sizing: border-box;
							height: 192px;
							.name {
								padding: 0 10px 0 0;
								margin: 0;
								overflow: hidden;
								color: #404040;
								white-space: nowrap;
								font-weight: 900;
								width: 100%;
								font-size: 15px;
								line-height: 24px;
								text-overflow: ellipsis;
								box-sizing: border-box;
								height: 24px;
							}
							.price {
								margin: 5px 0 0;
								color: #f00;
								font-size: 16px;
							}
							.desc {
								border: 1px dashed #dadada;
								padding: 5px 10px 0 0;
								margin: 5px 0 0;
								overflow: hidden;
								color: #808080;
								font-size: 14px;
								border-width: 1px 0 0;
								line-height: 24px;
								box-sizing: border-box;
								height: 48px;
							}
							.bottom {
								margin: 0;
								overflow: hidden;
								background: none;
								bottom: 5px;
								display: flex;
								width: calc(100% - 20px);
								justify-content: space-between;
								position: absolute;
								.publisher {
									color: #666;
									width: calc(100% - 110px);
									font-size: 14px;
								}
								.time {
									color: #999;
									display: inline;
									width: 110px;
									font-size: 14px;
									line-height: 24px;
									text-align: right;
									height: 24px;
								}
							}
							.jian {
								margin: -7px 0 0;
								clip-path: polygon(0% 0%, 100% 50%, 0% 100%);
								top: 50%;
								background: #fcfcfc;
								width: 9px;
								position: absolute;
								right: -9px;
								height: 14px;
							}
						}
					}
					.list-item2:hover {
						.img {
							img {
								transform: scale(1.05);
							}
						}
						.infoBox {
							background: #03cce9;
							.name {
								color: #fff;
							}
							.price {
								color: #fff;
							}
							.desc {
								color: #fff;
								border-color: #dadada;
							}
							.bottom {
								.publisher {
									color: #fff;
								}
								.time {
									color: #eee;
								}
							}
							.jian {
								background: #03cce9;
							}
						}
					}
					.list-item3 {
						cursor: pointer;
						margin: 0 0 6px;
						display: flex;
						width: 100%;
						.img {
							border: 1px solid #eee;
							z-index: 50;
							overflow: hidden;
							width: 50%;
							position: relative;
							height: 192px;
							img {
								object-fit: cover;
								display: block;
								width: 100%;
								transition: all 0.3s;
								height: 100%;
							}
						}
						.infoBox {
							padding: 5px 10px 0 10px;
							z-index: 100;
							background: #fcfcfc;
							width: 50%;
							position: relative;
							box-sizing: border-box;
							height: 192px;
							.name {
								padding: 0 10px 0 0;
								margin: 0;
								overflow: hidden;
								color: #404040;
								white-space: nowrap;
								font-weight: 900;
								width: 100%;
								font-size: 15px;
								line-height: 24px;
								text-overflow: ellipsis;
								box-sizing: border-box;
								height: 24px;
							}
							.price {
								margin: 5px 0 0;
								color: #f00;
								font-size: 16px;
							}
							.desc {
								border: 1px dashed #dadada;
								padding: 5px 10px 0 0;
								margin: 5px 0 0;
								overflow: hidden;
								color: #808080;
								font-size: 14px;
								border-width: 1px 0 0;
								line-height: 24px;
								box-sizing: border-box;
								height: 48px;
							}
							.bottom {
								margin: 0;
								overflow: hidden;
								background: none;
								bottom: 5px;
								display: flex;
								width: calc(100% - 20px);
								justify-content: space-between;
								position: absolute;
								.publisher {
									color: #666;
									width: calc(100% - 110px);
									font-size: 14px;
								}
								.time {
									color: #747474;
									display: inline;
									width: 110px;
									font-size: 14px;
									line-height: 28px;
									text-align: right;
									height: 28px;
								}
							}
							.jian {
								margin: -7px 0 0;
								clip-path: polygon(100% 1%, 100% 100%, 0% 50%);
								top: 50%;
								left: -8px;
								background: #fcfcfc;
								width: 9px;
								position: absolute;
								height: 14px;
							}
						}
					}
					.list-item3:hover {
						.img {
							img {
								transform: scale(1.05);
							}
						}
						.infoBox {
							background: #03cce9;
							.name {
								color: #fff;
							}
							.price {
								color: #fff;
							}
							.desc {
								color: #fff;
								border-color: #dadada;
							}
							.bottom {
								.publisher {
									color: #fff;
								}
								.time {
									color: #eee;
								}
							}
							.jian {
								background: #03cce9;
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0;
				cursor: pointer;
				margin: 40px auto;
				top: 0;
				background: #f7db61;
				display: block;
				width: 110px;
				line-height: 32px;
				position: absolute;
				right: calc((100% - 1200px)/2);
				text-align: center;
				.text {
					color: #333;
					font-size: 15px;
				}
				.icon {
					color: #333;
					font-size: 15px;
				}
			}
		}
	}
</style>

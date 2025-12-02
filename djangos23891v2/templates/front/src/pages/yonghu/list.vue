<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'>'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div v-if="centerType" class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span>返回</span>
			</el-button>
		</div>
		<div class="list-preview">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="list-item">
					<div class="lable">用户账号：</div>
					<el-input v-model="formSearch.yonghuzhanghao" placeholder="用户账号" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-form-item class="list-item">
					<div class="lable">用户姓名：</div>
					<el-input v-model="formSearch.yonghuxingming" placeholder="用户姓名" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-button class="list-search-btn" v-if=" true " type="primary" @click="getList(1, curFenlei)">
					<i class="el-icon-search"></i>
					查询
				</el-button>
				<el-button class="list-add-btn" v-if="btnAuth('yonghu','新增')" type="primary" @click="add('/index/yonghuAdd')">
					<i class="el-icon-circle-plus-outline"></i>
					添加
				</el-button>
			</el-form>
			<div class="select2">
				<div class="select2-list" v-for="(item,index) in selectOptionsList" :key="item">
					<div class="label">{{item.name}}：</div>
					<div class="item-body">
						<div class="item" @click="selectClick2(item,-1)" :class="item.check ==-1 ? 'active' : ''">全部</div>
						<div class="item" @click="selectClick2(item,index1)" :class="item.check == index1 ? 'active' : ''" v-for="item1,index1 in item.list" :key="item1">{{item1}}</div>
					</div>
				</div>
			</div>
			<div class="list">
				<div class="list5">
					<div v-for="(item,index) in dataList" :key="index" class="list-item" @click.stop="toDetail(item)">
						<div class="imgbox">
							<img @click.stop="imgPreView(item.touxiang.split(',')[0])" v-if="item.touxiang && item.touxiang.substr(0,4)=='http'" :src="item.touxiang.split(',')[0]" class="image" />
							<img @click.stop="imgPreView(baseUrl + (item.touxiang?item.touxiang.split(',')[0]:''))" v-else :src="baseUrl + (item.touxiang?item.touxiang.split(',')[0]:'')" class="image" />
						</div>
						<div class="infoBox">
							<div class="name">{{item.yonghuxingming}}</div>
							<div class="bottomInfo">
								<div class="time_item">
									<span class="icon iconfont "></span>
									<span class="label">发布时间：</span>
									<span class="text">{{item.addtime.split(' ')[0]}}</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

	
			<el-pagination
				background
				id="pagination"
				class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				prev-text="上一页"
				next-text="下一页"
				:hide-on-single-page="false"
				:layout='["total","prev","pager","next","sizes","jumper"].join()'
				:total="total"
				:page-sizes="pageSizes"
				@current-change="curChange"
				@size-change="sizeChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>
			<div class="idea1"></div>
		</div>
		<el-dialog title="预览图" :visible.sync="previewVisible" width="50%">
			<img :src="previewImg" alt="" style="width: 100%;">
		</el-dialog>
	</div>
</template>
<script>
	export default {
		//数据集合
		data() {
			return {
				selectIndex2: 0,
				selectOptionsList: [],
				layouts: '',
				swiperIndex: -1,
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '用户'
					}
				],
				formSearch: {
					yonghuzhanghao: '',
					yonghuxingming: '',
				},
				fenlei: [],
				feileiColumn: '',
				dataList: [],
				total: 1,
				pageSize: 12,
				pageSizes: [],
				totalPage: 1,
				curFenlei: '全部',
				isPlain: false,
				indexQueryCondition: '',
				timeRange: [],
				centerType:false,
				previewImg: '',
				previewVisible: false,
				sortType: 'id',
				sortOrder: 'desc',
			}
		},
		async created() {
			if(this.$route.query.centerType){
				this.centerType = true
			}
			this.baseUrl = this.$config.baseUrl;
			await this.getFenlei();
			let fenlei = '全部'
			if(this.$route.query.homeFenlei){
				fenlei = this.$route.query.homeFenlei
			}
			this.getList(1, fenlei);
		},
		watch:{
			$route(newValue){
				this.getList(1, newValue.query.homeFenlei);
			}
		},
		//方法集合
		methods: {
			selectClick2(row,index) {
				row.check = index
				if(index == -1){
					this.formSearch[row.tableName] = ''
				}else {
					this.formSearch[row.tableName] = row.list[index]
				}
				this.getList()
			},
			add(path) {
				let query = {}
				if(this.centerType){
					query.centerType = 1
				}
				this.$router.push({path: path,query:query});
			},
			async getFenlei() {
			},
			getList(page, fenlei, ref = '') {
				let params = {
					page,
					limit: this.pageSize,
				};
				let searchWhere = {};
				if (this.formSearch.yonghuzhanghao != '') searchWhere.yonghuzhanghao = '%' + this.formSearch.yonghuzhanghao + '%';
				if (this.formSearch.yonghuxingming != '') searchWhere.yonghuxingming = '%' + this.formSearch.yonghuxingming + '%';
				let user = JSON.parse(localStorage.getItem('sessionForm'))
				if (this.sortType) searchWhere.sort = this.sortType
				if (this.sortOrder) searchWhere.order = this.sortOrder
				this.$http.get(`yonghu/${this.centerType?'page':'list'}`, {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.dataList = res.data.data.list;
						this.total = Number(res.data.data.total);
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			curChange(page) {
				this.getList(page);
			},
			prevClick(page) {
				this.getList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getList(1);
			},
			nextClick(page) {
				this.getList(page);
			},
			imgPreView(url){
				this.previewImg = url
				this.previewVisible = true
			},
			toDetail(item) {
				let params = {
					id: item.id
				}
				if(this.centerType){
					params.centerType = 1
				}
				this.$router.push({path: '/index/yonghuDetail', query: params});
			},
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			backClick() {
				this.$router.push({path: '/index/center'});
			},
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.list-preview {
		margin: 0px auto;
		flex-direction: column;
		color: #333;
		background: none;
		display: flex;
		width: 1200px;
		font-size: 16px;
		justify-content: flex-start;
		align-items: flex-start;
		position: relative;
		flex-wrap: wrap;
		.list-form-pv {
			padding: 0;
			margin: 20px 0;
			color: inherit;
			background: none;
			display: flex;
			width: 100%;
			font-size: inherit;
			flex-wrap: wrap;
			height: auto;
			.list-item {
				padding: 0;
				margin: 0 0px 10px 0;
				display: flex;
				font-size: inherit;
				align-items: center;
				flex-wrap: wrap;
				.lable {
					padding: 0 10px;
					color: #333;
					white-space: nowrap;
					display: inline-block;
					width: auto;
					font-size: 16px;
					line-height: 40px;
				}
				.el-input {
					width: auto;
				}
				.datetimerange {
					border: 1px solid #ccc;
					border-radius: 8px;
					padding: 3px 3px;
					background: #fff;
					width: auto;
					justify-content: center;
				}
				.el-input /deep/ .el-input__inner {
					border: 1px solid #ccc;
					border-radius: 4px;
					padding: 0 10px;
					margin: 0 5px 0 0;
					color: #333;
					width: auto;
					font-size: 16px;
					line-height: 40px;
					height: 40px;
				}
				.el-select {
				}
				.el-select /deep/ .el-input__inner {
				}
				.el-date-editor {
					width: auto;
				}
				.el-date-editor /deep/ .el-input__inner {
					border: 1px solid #ccc;
					border-radius: 4px;
					padding: 0 0px 0 30px;
					margin: 0;
					color: #333;
					width: auto;
					font-size: 16px;
					line-height: 40px;
					height: 40px;
				}
			}
			.list-search-btn {
				cursor: pointer;
				border: 0;
				border-radius: 4px;
				padding: 0px 15px;
				margin: 0 10px 0 10px;
				color: #fff;
				background: #018cc0;
				width: auto;
				font-size: inherit;
				line-height: 40px;
				height: 40px;
				i {
					margin: 0 10px 0 0;
					color: #fff;
					font-size: inherit;
				}
			}
			.list-add-btn {
				cursor: pointer;
				border: 0;
				border-radius: 4px;
				padding: 0px 15px;
				margin: 0 10px 0 0;
				color: #fff;
				background: #03cce9;
				width: auto;
				font-size: inherit;
				line-height: 40px;
				height: 40px;
				i {
					margin: 0 10px 0 0;
					color: #fff;
					font-size: inherit;
				}
			}
		}
		.select2 {
			padding: 0;
			margin: 20px auto;
			background: none;
			width: 100%;
			font-size: 15px;
			height: auto;
			.select2-list {
				padding: 5px 5px;
				margin: 0 0 10px;
				background: none;
				width: 100%;
				height: auto;
				.label {
					padding: 0 5px;
					color: #333;
					font-weight: 500;
					display: inline-block;
					font-size: inherit;
					line-height: 32px;
				}
				.item-body {
					display: inline-block;
					width: auto;
					flex-wrap: wrap;
					height: auto;
					.item {
						border-radius: 4px;
						padding: 0 5px;
						color: inherit;
						background: none;
						display: inline-block;
						font-size: inherit;
						line-height: 32px;
						text-align: center;
						min-width: 50px;
					}
					.item:hover {
						cursor: pointer;
						color: #fff;
						background: #03cce9;
					}
					.item.active {
						cursor: pointer;
						color: #fff;
						background: #03cce9;
						display: inline-block;
						min-width: 50px;
						text-align: center;
					}
				}
			}
		}
		.list {
			margin: 20px auto;
			overflow: hidden;
			background: #fff;
			width: 100%;
			clear: both;
			font-size: 15px;
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
				
			.index-pv1 .animation-box:hover {
				transform: rotate(0) scale(1.2) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
				
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0) scale(0.8) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list5 {
				column-gap: 15px;
				margin: 10px auto;
				column-count: 4;
				width: 1200px;
				.list-item {
					border: 1px solid #eee;
					padding: 10px;
					margin: 0 0 20px;
					overflow: hidden;
					background: #fff;
					display: block;
					position: relative;
					.imgbox {
						overflow: hidden;
						width: 100%;
						.image {
							filter: saturate(150%);
							transform: rotate(0deg);
							display: block;
							width: 100%;
							opacity: 0.9;
						}
					}
					.infoBox {
						padding: 10px 10px;
						left: 0px;
						bottom: 0;
						background: rgba(255, 255, 255, .8);
						width: 100%;
						font-size: 16px;
						position: inherit;
						transition: all 0.5s;
						.name {
							overflow: hidden;
							color: #666;
							white-space: nowrap;
							font-weight: 600;
							width: 100%;
							font-size: 16px;
							line-height: 24px;
							text-overflow: ellipsis;
						}
						.price {
							color: #666;
							font-size: 14px;
							.price_text {
								color: #f00;
								font-size: 18px;
							}
						}
						.bottomInfo {
							margin: 5px 0 0;
							color: #888;
							display: flex;
							font-size: 15px;
							flex-wrap: wrap;
							.time_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
								.label {
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
								.text {
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0;
								margin: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
								.label {
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
								.text {
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0;
								margin: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
								.label {
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
								.text {
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0;
								margin: 0 10px 0 0;
								.icon {
									margin: 0 2px 0 0;
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
								.label {
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
								.text {
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
								.label {
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
								.text {
									color: inherit;
									font-size: inherit;
									line-height: 1.5;
								}
							}
						}
					}
				}
				.list-item:hover {
					border: 1px solid #03cce9;
					cursor: pointer;
					background: #03cce9;
					.imgbox {
						.image {
							transform: scale(1.05);
							ilter: saturate(100%);
							opacity: 1;
							transition: all 200ms linear;
						}
					}
					.infoBox {
						bottom: 0px;
						background: #fff;
						font-size: 16px;
						.name {
							color: #000;
						}
						.price {
							color: #000;
							.price_text {
							}
						}
						.bottomInfo {
							margin: 5px 0 0;
							color: #888;
							display: flex;
							font-size: 15px;
							flex-wrap: wrap;
							.time_item {
								.icon {
									color: #000;
								}
								.label {
									color: #000;
								}
								.text {
									color: #000;
								}
							}
							.publisher_item {
								.icon {
									color: #000;
								}
								.label {
									color: #000;
								}
								.text {
									color: #000;
								}
							}
							.like_item {
								.icon {
									color: #000;
								}
								.label {
									color: #000;
								}
								.text {
									color: #000;
								}
							}
							.collect_item {
								.icon {
									color: #000;
								}
								.label {
									color: #000;
								}
								.text {
									color: #000;
								}
							}
							.view_item {
								.icon {
									color: #000;
								}
								.label {
									color: #000;
								}
								.text {
									color: #000;
								}
							}
						}
					}
				}
			}
		}
		.idea1 {
			background: none;
			width: 100%;
			order: 90;
			height: 1px;
		}
	}
</style>

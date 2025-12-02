<template>
	<div class="navbar">
		<div class="title">
			<span class="title-name">{{this.$project.projectName}}</span>
		</div>
		<div class="btn-box">
			<el-button class="go-btn" type="primary" @click="goClick">
				<span class="icon iconfont icon-jiantou34"></span>
				前进
			</el-button>
			<el-button class="back-btn" type="primary" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				后退
			</el-button>
			<el-button class="refresh-btn" type="primary" @click="refreshClick">
				<span class="icon iconfont icon-shuaxin"></span>
				刷新
			</el-button>
			<el-button class="loginout-btn" type="primary" @click="onLogout">
				<span class="icon iconfont icon-guanbi19"></span>
				退出
			</el-button>
		</div>
		<el-dropdown class="dropdown-box" @command="handleCommand" trigger="click">
			<div class="el-dropdown-link">
				<el-image v-if="user" :src="avatar?this.$base.url + avatar : require('@/assets/img/avator.png')" fit="cover"></el-image>
				<span class="label">欢迎您，</span>
				<span class="nickname">{{this.$storage.get('adminName')}}</span>
				<span class="icon iconfont icon-xiala"></span>
			</div>
			<el-dropdown-menu class="top-el-dropdown-menu" slot="dropdown">
				<el-dropdown-item class="item1" :command="''">
					<span class="icon iconfont icon-home7"></span>
					首页
				</el-dropdown-item>
				<el-dropdown-item class="item2" :command="'center'">
					<span class="icon iconfont icon-touxiang03"></span>
					个人中心
				</el-dropdown-item>
				<el-dropdown-item v-if="this.$storage.get('role')!='管理员'" class="item3" :command="'front'">
					<span class="icon iconfont icon-guanbi19"></span>
					退出到前台
				</el-dropdown-item>
				<el-dropdown-item v-if="isAuth('hasBoard','查看')" class="item3" :command="'board'">
					<span class="icon iconfont icon-guanbi19"></span>
					看板
				</el-dropdown-item>
				<el-dropdown-item v-if="this.$storage.get('role')=='管理员'" class="item3" :command="'backUp'">
					<span class="icon iconfont icon-guanbi19"></span>
					数据备份
				</el-dropdown-item>
				<el-dropdown-item v-if="this.$storage.get('role')=='管理员'" class="item3" :command="'analyze'">
					<span class="icon iconfont icon-guanbi19"></span>
					数据分析
				</el-dropdown-item>
				<el-dropdown-item class="item4" :command="'logout'">
					<span class="icon iconfont icon-fanhui14"></span>
					退出登录
				</el-dropdown-item>
			</el-dropdown-menu>
		</el-dropdown>
	</div>
</template>

<script>
	import {
		Loading
	} from 'element-ui';
	import axios from 'axios';
	export default {
		data() {
			return {
				dialogVisible: false,
				ruleForm: {},
				user: null,
			};
		},
		created() {
			// 获取天气
			this.getWeather()
		},
		computed: {
			avatar(){
				return this.$storage.get('headportrait')?this.$storage.get('headportrait'):''
			},
		},
		mounted() {
			let sessionTable = this.$storage.get("sessionTable")
			this.$http({
				url: sessionTable + '/session',
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code === 0) {
					if(sessionTable == 'yonghu') {
						this.$storage.set('headportrait',data.data.touxiang)
					}
					if(sessionTable == 'users') {
						this.$storage.set('headportrait',data.data.image)
					}
					this.$storage.set('userForm',JSON.stringify(data.data))
					this.user = data.data;
					this.$storage.set('userid',data.data.id);
				} else {
					let message = this.$message
					message.error(data.msg);
				}
			});
		},
		methods: {
			// 前进
			goClick(){
				history.go(1)
			},
			// 后退
			backClick(){
				history.go(-1)
			},
			// 刷新
			refreshClick(){
				window.location.reload()
			},
			// 获取当前城市天气
			getWeather(){
				axios({
					method: 'get',
					url: 'http://v0.yiketianqi.com/free/day?appid=69475998&appsecret=rldbX1Zl'
				}).then(res => {
					let d = new Date()
					let times = d.getFullYear() + '-' + ((d.getMonth() + 1)<10?('0' + (d.getMonth() + 1)):(d.getMonth() + 1)) + '-' + (d.getDate()<10?('0' + d.getDate()):d.getDate()) + ' ' + (d.getHours()<10?('0' + d.getHours()):d.getHours()) + ':' + (d.getMinutes()<10?('0' + d.getMinutes()):d.getMinutes()) + ':' + (d.getSeconds()<10?('0' + d.getSeconds()):d.getSeconds())
					this.$storage.set('nowLocation',res.data.city)
					this.$storage.set('nowTime',times)
				})
			},
			handleCommand(name) {
				if (name == 'logout') {
					this.onLogout()
				} 
				else if (name == 'front') {
					this.onIndexTap()
				}
				else if (name == 'board'){
					this.toBoard()
				}
				else if (name == 'backUp'){
					this.backUp()
				}
				else if (name == 'analyze'){
					this.analyzeClick()
				}
				else {
					let router = this.$router
					name = '/'+name
					router.push(name)
				}
			},
			onLogout() {
				let storage = this.$storage
				let router = this.$router
				let location = storage.get('nowLocation')
				let times = storage.get('nowTime')
				storage.clear()
				this.$store.dispatch('tagsView/delAllViews')
				this.$storage.set('nowLocation',location)
				this.$storage.set('nowTime',times)
				router.replace({
					name: "login"
				});
			},
			onIndexTap(){
				window.location.href = `${this.$base.indexUrl}`
			},
			toBoard(){
				let routeData = this.$router.resolve({ path: '/board'});
				window.open(routeData.href, '_blank');
			},
			analyzeClick() {
				this.$confirm('是否进行大数据分析?', '数据分析提示', {
					confirmButtonText: '是',
					cancelButtonText: '否',
					type: 'warning'
				}).then(() => {
					let loading = null;
					loading = Loading.service({
						target: this.$refs['roleMenuBox'],
						fullscreen: false,
						text: '数据分析中，请稍等...'
					})
					this.$http({
						url: '/hive/analyze',
						method: "get"
					}).then(({
						data
					}) => {
						if(loading) loading.close()
						if(data.code==0){
							this.$message({
								message: '数据分析完成',
								type: 'success',
								duration: 1500,
							});
						}
					},err=>{
						if(loading) loading.close()
					});
				});
			},
			backUp() {
				this.$confirm('是否备份数据库?', '数据备份提示', {
					confirmButtonText: '是',
					cancelButtonText: '否',
					type: 'warning'
				}).then(() => {
					this.$http({
						url: '/mysqldump',
						method: "get"
					}).then(({
						data
					}) => {
						if (data) {
							const binaryData = [];
							binaryData.push(data);
							const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
								type: 'application/pdf;chartset=UTF-8'
							}))
							const a = document.createElement('a')
							a.href = objectUrl
							a.download = 'mysql.dmp'
							// a.click()
							// 下面这个写法兼容火狐
							a.dispatchEvent(new MouseEvent('click', {
								bubbles: true,
								cancelable: true,
								view: window
							}))
							window.URL.revokeObjectURL(data)
							message.message("数据备份成功")
						} else {
							let message = this.$message
							message.error(data.msg);
						}
					});
				});
			},
		}
	};
</script>


<style lang="scss" scoped>
	.navbar {
		.title {
			display: none;
			.title-name {
				padding: 0 0 0 12px;
				color: rgba(64, 158, 255, 1);
				line-height: 44px;
				float: left;
			}
		}
		.btn-box {
			left: 210px;
			display: flex;
			width: auto;
			position: absolute;
			order: -1;
			// 前进
			.go-btn {
				border: 0;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 5px;
				margin: 0 5px 0 0;
				color: rgba(255, 255, 255, 1);
				background: linear-gradient(180deg, rgba(24,161,192,1) 0%, rgba(24,161,192,1) 50%, rgba(6,98,118,1) 50%, rgba(6,98,118,1) 100%);
				width: auto;
				font-size: 12px;
				line-height: 20px;
				height: 20px;
				.iconfont {
					margin: 0 0px 0 0;
					color: rgba(255, 255, 255, 1);
					font-size: 12px;
				}
			}
			.go-btn:hover {
				opacity: 1;
			}
			// 后退
			.back-btn {
				border: 0;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 10px;
				margin: 0 5px 0 0;
				color: rgba(255, 255, 255, 1);
				background: linear-gradient(180deg, rgba(24,161,192,1) 0%, rgba(24,161,192,1) 50%, rgba(6,98,118,1) 50%, rgba(6,98,118,1) 100%);
				width: auto;
				font-size: 12px;
				line-height: 20px;
				height: 20px;
				.iconfont {
					margin: 0 0px 0 0;
					color: rgba(255, 255, 255, 1);
					font-size: 12px;
				}
			}
			.back-btn:hover {
				opacity: 1;
			}
			// 刷新
			.refresh-btn {
				border: 0;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 10px;
				margin: 0 5px 0 0;
				color: rgba(255, 255, 255, 1);
				background: linear-gradient(180deg, rgba(24,161,192,1) 0%, rgba(24,161,192,1) 50%, rgba(6,98,118,1) 50%, rgba(6,98,118,1) 100%);
				width: auto;
				font-size: 12px;
				line-height: 20px;
				height: 20px;
				.iconfont {
					margin: 0 0px 0 0;
					color: rgba(255, 255, 255, 1);
					font-size: 12px;
				}
			}
			.refresh-btn:hover {
				opacity: 1;
			}
			// 退出
			.loginout-btn {
				border: 0;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 10px;
				margin: 0 5px 0 0;
				color: rgba(255, 255, 255, 1);
				background: linear-gradient(180deg, rgba(24,161,192,1) 0%, rgba(24,161,192,1) 50%, rgba(6,98,118,1) 50%, rgba(6,98,118,1) 100%);
				width: auto;
				font-size: 12px;
				line-height: 20px;
				height: 20px;
				.iconfont {
					margin: 0 0px 0 0;
					color: rgba(255, 255, 255, 1);
					font-size: 12px;
				}
			}
			.loginout-btn:hover {
				opacity: 1;
			}
		}
		.dropdown-box {
			color: #fff;
			display: flex;
			font-size: 14px;
			right: 20px;
			.el-dropdown-link {
				display: flex;
				align-items: center;
				.el-image {
					border-radius: 100%;
					margin: 0 10px;
					object-fit: cover;
					display: inline-block;
					width: 32px;
					height: 32px;
				}
				.label {
					color: #fff;
					font-size: 14px;
					line-height: 32px;
				}
				.nickname {
					color: #fff;
					font-size: 14px;
					line-height: 32px;
				}
				.iconfont {
					margin: 0 0 0 5px;
					color: rgba(255,255,255,.6);
					font-size: 14px;
				}
			}
			.top-el-dropdown-menu {
				border: 1px solid #EBEEF5;
				border-radius: 4px;
				padding: 10px 0;
				box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
				margin: 18px 0;
				background: #FFF;
				li.el-dropdown-menu__item.item1 {
					cursor: pointer;
					padding: 0 20px;
					margin: 0;
					outline: 0;
					color: #606266;
					background: #fff;
					font-size: 14px;
					line-height: 36px;
					list-style: none;
					.iconfont {
						margin: 0 4px 0 0;
							color: #000;
							font-size: 14px;
						}
				}
				li.el-dropdown-menu__item.item1:hover {
					background: #ecf5ff;
				}
				li.el-dropdown-menu__item.item2 {
					cursor: pointer;
					padding: 0 20px;
					margin: 0;
					outline: 0;
					color: #606266;
					background: #fff;
					font-size: 14px;
					line-height: 36px;
					list-style: none;
					.iconfont {
						margin: 0 4px 0 0;
							color: #000;
							font-size: 14px;
						}
				}
				li.el-dropdown-menu__item.item2:hover {
					background: #ecf5ff;
				}
				li.el-dropdown-menu__item.item3 {
					cursor: pointer;
					padding: 0 20px;
					margin: 0;
					outline: 0;
					color: #606266;
					background: #fff;
					font-size: 14px;
					line-height: 36px;
					list-style: none;
					.iconfont {
						margin: 0 4px 0 0;
						color: #000;
						font-size: 14px;
					}
				}
				li.el-dropdown-menu__item.item3:hover {
					background: #ecf5ff;
				}
				li.el-dropdown-menu__item.item4 {
					cursor: pointer;
					padding: 0 20px;
					margin: 0;
					outline: 0;
					color: #606266;
					background: #fff;
					font-size: 14px;
					line-height: 36px;
					list-style: none;
					.iconfont {
						margin: 0 4px 0 0;
						color: #000;
						font-size: 14px;
					}
				}
				li.el-dropdown-menu__item.item4:hover {
					background: #ecf5ff;
				}
			}
		}
	}
</style>

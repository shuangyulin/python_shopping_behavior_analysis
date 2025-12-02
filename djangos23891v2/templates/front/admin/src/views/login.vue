<template>
	<div>
		<div class="login-container">
			<el-form class="login_form animate__animated animate__">
				<div class="login_form2">
					<div class="title-container">基于Python的电商用户行为分析系统</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							账号：
						</div>
						<input placeholder="请输入账号：" name="username" type="text" v-model="rulesForm.username">
					</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							密码：
						</div>
						<div class="password-box">
							<input placeholder="请输入密码：" name="password" :type="showPassword?'text':'password'" v-model="rulesForm.password">
							<span class="icon iconfont" :class="showPassword?'icon-liulan13':'icon-liulan17'" @click="showPassword=!showPassword"></span>
						</div>
					</div>

					<div class="list-item " v-if="roles.length>1">
						<div class="lable">
							角色：
						</div>
						<div prop="loginInRole" class="list-type">
							<el-radio v-if="loginType==1||(loginType==2&&item.roleName!='管理员')" v-for="item in roles" v-bind:key="item.roleName" v-model="rulesForm.role" :label="item.roleName">{{item.roleName}}</el-radio>
						</div>
					</div>

		
					<div class="login-btn">
						<div class="login-btn1">
							<el-button v-if="loginType==1" type="primary" @click="login()" class="loginInBt">登录</el-button>
						</div>
						<div class="login-btn2">
						</div>
						<div class="login-btn3">
						</div>
					</div>
				</div>
				<div class="idea-box1"></div>
			</el-form>
		</div>
	</div>
</template>
<script>
	import 'animate.css'
	import menu from "@/utils/menu";
	export default {
		data() {
			return {
				verifyCheck2: false,
				flag: false,
				baseUrl:this.$base.url,
				loginType: 1,
				rulesForm: {
					username: "",
					password: "",
					role: "",
				},
				menus: [],
				roles: [],
				tableName: "",
				showPassword: false,
			};
		},
		mounted() {
			let menus = menu.list();
			this.menus = menus;

			for (let i = 0; i < this.menus.length; i++) {
				if (this.menus[i].hasBackLogin=='是') {
					this.roles.push(this.menus[i])
				}
			}

		},
		created() {

		},
		destroyed() {
		},
		components: {
		},
		methods: {

			//注册
			register(tableName){
				this.$storage.set("loginTable", tableName);
				this.$router.push({path:'/register',query:{pageFlag:'register'}})
			},
			// 登陆
			login() {

				if (!this.rulesForm.username) {
					this.$message.error("请输入用户名");
					return;
				}
				if (!this.rulesForm.password) {
					this.$message.error("请输入密码");
					return;
				}
				if(this.roles.length>1) {
					if (!this.rulesForm.role) {
						this.$message.error("请选择角色");
						return;
					}

					let menus = this.menus;
					for (let i = 0; i < menus.length; i++) {
						if (menus[i].roleName == this.rulesForm.role) {
							this.tableName = menus[i].tableName;
						}
					}
				} else {
					this.tableName = this.roles[0].tableName;
					this.rulesForm.role = this.roles[0].roleName;
				}
		
				this.loginPost()
			},
			loginPost() {
				this.$http({
					url: `${this.tableName}/login?username=${this.rulesForm.username}&password=${this.rulesForm.password}`,
					method: "post"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						if(this.$storage.get('nowLocation')){
							let location = this.$storage.get('nowLocation')
							this.$storage.set('beforeLocation',location)
						}
						if(this.$storage.get('nowTime')){
							let times = this.$storage.get('nowTime')
							this.$storage.set('beforeTime',times)
						}
						this.$storage.set("Token", data.token);
						this.$storage.set("role", this.rulesForm.role);
						this.$storage.set("sessionTable", this.tableName);
						this.$storage.set("adminName", this.rulesForm.username);
						if(this.boardAuth('hasBoard','查看',this.rulesForm.role)) {
							this.$router.replace({ path: "/board" });
						}else {
							this.$router.replace({ path: "/" });
						}
					} else {
						this.$message.error(data.msg);
					}
				});
			},
		}
	}
</script>

<style lang="scss" scoped>
.login-container {
	min-height: 100vh;
	position: relative;
	background-repeat: no-repeat;
	background-position: center center;
	background-size: cover;
	background: url(http://codegen.caihongy.cn/20240712/b8908b2889424c4bb79758bad47902c8.jpg);
	background-repeat: no-repeat;
	background-size: cover;
	background: url(http://codegen.caihongy.cn/20240712/b8908b2889424c4bb79758bad47902c8.jpg);
	display: flex;
	width: 100%;
	min-height: 100vh;
	justify-content: center;
	align-items: center;
	background-position: center center;

	.login_form {
		border-radius: 30px;
		padding: 40px 20px 150px;
		box-shadow: inset 0px 0px 0px 0px #000;
		margin: 0;
		z-index: 1000;
		background: url(http://codegen.caihongy.cn/20240712/20524ce2c9594a3b9dcc1f32bbf3c59e.png) no-repeat center top / 100% 100%;
		width: 500px;
		min-height: 500px;
		position: relative;
		height: auto;
		.login_form2 {
			width: 100%;
		}
		.title-container {
			margin: 0 0 24px 0;
			color: #fff;
			background: url(http://codegen.caihongy.cn/20240712/005375b3a1f0412a8dce8131bb43ee06.png) no-repeat center top / 100% 100%;
			width: 100%;
			font-size: 16px;
			line-height: 40px;
			text-align: center;
		}
		.list-item {
			padding: 0;
			margin: 0 0 20px 120px;
			display: flex;
			width: calc(80% - 120px);
			align-items: center;
			position: relative;
			flex-wrap: wrap;
			.lable {
				color: #fff;
				left: -120px;
				width: 120px;
				font-size: 14px;
				line-height: 40px;
				position: absolute !important;
				text-align: right;
			}
			input {
				border: 0px solid rgba(0, 0, 0, 1);
				padding: 0 10px;
				color: #666;
				width: 100%;
				font-size: 16px;
				height: 34px;
			}
			input:focus {
				border: 0px solid rgba(85, 170, 0, 1.0);
				padding: 0 10px;
				color: #666;
				width: 100%;
				font-size: 16px;
				height: 34px;
			}
			.password-box {
				display: flex;
				width: 100%;
				position: relative;
				align-items: center;
				input {
					border: 0px solid rgba(0, 0, 0, 1);
					padding: 0 10px;
					color: #666;
					width: 100%;
					font-size: 16px;
					height: 34px;
				}
				input:focus {
					border: 0px solid rgba(85, 170, 0, 1.0);
					padding: 0 10px;
					color: #666;
					width: 100%;
					font-size: 16px;
					height: 34px;
				}
				.iconfont {
					cursor: pointer;
					z-index: 1;
					color: #000;
					top: 0;
					font-size: 16px;
					line-height: 44px;
					position: absolute;
					right: 5px;
				}
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
		}
		.list-type {
			padding: 0;
			margin: 0;
			background: none;
			width: calc(100% - 10px);
			line-height: 40px;
			height: auto;
			/deep/ .el-radio__input .el-radio__inner {
				background: rgba(53, 53, 53, 0);
				border-color: #fff;
			}
			/deep/ .el-radio__input.is-checked .el-radio__inner {
				background: rgba(85, 170, 0, 1.0);
				border-color: rgba(85, 170, 0, 1.0);
			}
			/deep/ .el-radio__label {
				color: #fff;
				font-size: 16px;
			}
			/deep/ .el-radio__input.is-checked+.el-radio__label {
				color: #b6db61;
				font-size: 16px;
			}
		}
		.login-btn {
			margin: 20px auto;
			display: flex;
			width: 80%;
			justify-content: center;
			align-items: center;
			flex-wrap: wrap;
			.login-btn1 {
				width: auto;
			}
			.login-btn2 {
				width: auto;
			}
			.login-btn3 {
				width: auto;
			}
			.loginInBt {
				border: 2px solid rgba(0, 0, 0, 1);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 10px;
				margin: 0 5px 10px;
				color: rgba(0, 0, 0, 1);
				background: #fff;
				width: auto;
				font-size: 16px;
				min-width: 68px;
				height: 34px;
			}
			.loginInBt:hover {
				border: 2px solid rgba(85, 170, 0, 1.0);
				color: rgba(85, 170, 0, 1.0);
				opacity: 1;
			}
			.register {
				border: 2px solid rgba(0, 0, 0, 1);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 10px;
				margin: 0 5px 10px;
				color: rgba(0, 0, 0, 1);
				background: #fff;
				width: auto;
				font-size: 16px;
				height: 34px;
			}
			.register:hover {
				border: 2px solid rgba(85, 170, 0, 1.0);
				color: rgba(85, 170, 0, 1.0);
				opacity: 1;
			}
			.forget {
				border: 0;
				cursor: pointer;
				border-radius: 0;
				padding: 0;
				margin: 0 5px 10px;
				color: #fff;
				background: none;
				width: auto;
				font-size: 16px;
				height: 34px;
			}
			.forget:hover {
				opacity: 1;
			}
		}
	}
	.idea-box1 {
		z-index: 1111;
		top: 15px;
		background: url(http://codegen.caihongy.cn/20240712/e60eeb01929043588a299c3af86cdd1b.png) no-repeat;
		width: 124px;
		position: absolute;
		right: -50px;
		height: 167px;
	}
}

</style>

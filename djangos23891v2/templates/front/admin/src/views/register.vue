<template>
	<div>
		<div class="register-container">
			<el-form v-if="pageFlag=='register'" ref="rgsForm" class="rgs-form animate__animated animate__" :model="rgsForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">基于Python的电商用户行为分析系统</div>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('yonghuzhanghao')?'required':''">用户账号：</div>
						<el-input  v-model="ruleForm.yonghuzhanghao"  autocomplete="off" placeholder="用户账号"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input  v-model="ruleForm.mima"  autocomplete="off" placeholder="密码"  type="password"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('yonghuxingming')?'required':''">用户姓名：</div>
						<el-input  v-model="ruleForm.yonghuxingming"  autocomplete="off" placeholder="用户姓名"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="ruleForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in yonghuxingbieOptions"
								v-bind:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('nianling')?'required':''">年龄：</div>
						<el-input  v-model.number="ruleForm.nianling"  autocomplete="off" placeholder="年龄"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('shouji')?'required':''">手机：</div>
						<el-input  v-model="ruleForm.shouji"  autocomplete="off" placeholder="手机"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="3"
							:multiple="true"
							:fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
							@change="yonghutouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<button type="button" class="r-btn" @click="login()">注册</button>
						</div>
						<div class="register-btn2">
							<div class="r-login" @click="close()">已有账号，直接登录</div>
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
export default {
	data() {
		return {
			ruleForm: {
			},
			forgetForm: {},
            pageFlag : '',
			tableName:"",
			rules: {},
            yonghuxingbieOptions: [],
		};
	},
	mounted(){
		this.pageFlag = this.$route.query.pageFlag
		if(this.$route.query.pageFlag=='register'){
			
			let table = this.$storage.get("loginTable");
			this.tableName = table;
			if(this.tableName=='yonghu'){
				this.ruleForm = {
					yonghuzhanghao: '',
					mima: '',
					yonghuxingming: '',
					xingbie: '',
					nianling: '',
					shouji: '',
					touxiang: '',
					money: '',
				}
			}
			if ('yonghu' == this.tableName) {
				this.rules.yonghuzhanghao = [{ required: true, message: '请输入用户账号', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.yonghuxingming = [{ required: true, message: '请输入用户姓名', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.xingbie = [{ required: true, message: '请输入性别', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.shouji = [{ required: true, message: '请输入手机', trigger: 'blur' }]
			}
			this.yonghuxingbieOptions = "男,女".split(',')
		}
	},
	created() {
	},
	destroyed() {
		  	},
	methods: {
		changeRules(name){
			if(this.rules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		close(){
			this.$router.push({ path: "/login" });
		},
        yonghutouxiangUploadChange(fileUrls) {
            this.ruleForm.touxiang = fileUrls;
        },

        // 多级联动参数


		// 注册
		login() {
			var url=this.tableName+"/register";
			if((!this.ruleForm.yonghuzhanghao) && `yonghu` == this.tableName){
				this.$message.error(`用户账号不能为空`);
				return
			}
			if((!this.ruleForm.mima) && `yonghu` == this.tableName){
				this.$message.error(`密码不能为空`);
				return
			}
			if((this.ruleForm.mima!=this.ruleForm.mima2) && `yonghu` == this.tableName){
				this.$message.error(`两次密码输入不一致`);
				return
			}
			if((!this.ruleForm.yonghuxingming) && `yonghu` == this.tableName){
				this.$message.error(`用户姓名不能为空`);
				return
			}
			if((!this.ruleForm.xingbie) && `yonghu` == this.tableName){
				this.$message.error(`性别不能为空`);
				return
			}
			if(`yonghu` == this.tableName && this.ruleForm.nianling &&(!this.$validate.isIntNumer(this.ruleForm.nianling))){
				this.$message.error(`年龄应输入整数`);
				return
			}
			if((!this.ruleForm.shouji) && `yonghu` == this.tableName){
				this.$message.error(`手机不能为空`);
				return
			}
			if(`yonghu` == this.tableName && this.ruleForm.shouji &&(!this.$validate.isMobile(this.ruleForm.shouji))){
				this.$message.error(`手机应输入手机格式`);
				return
			}
            if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
            }
			this.$http({
				url: url,
				method: "post",
				data:this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message({
						message: "注册成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.$router.replace({ path: "/login" });
						}
					});
				} else {
					this.$message.error(data.msg);
				}
			});
		}
	}
};
</script>

<style lang="scss" scoped>
.register-container {
	position: relative;
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
	.rgs-form {
		.rgs-form2 {
		width: 100%;
		}
		border-radius: 30px;
		padding: 40px 20px 240px;
		box-shadow: inset 0px 0px 0px 0px #000;
		margin: 20px auto;
		z-index: 1;
		background: url(http://codegen.caihongy.cn/20240712/20524ce2c9594a3b9dcc1f32bbf3c59e.png) no-repeat center top / 100% 100%;
		width: 500px;
		position: relative;
		height: auto;
		.title {
			margin: 0 0 20px 0;
			color: #fff;
			background: url(http://codegen.caihongy.cn/20240712/005375b3a1f0412a8dce8131bb43ee06.png) no-repeat center top / 100% 100%;
			width: 100%;
			font-size: 16px;
			line-height: 40px;
			text-align: center;
		}
		.list-item {
			padding: 0 0 0 0px;
			margin: 0 0 10px 120px;
			width: calc(80% - 120px);
			position: relative;
			height: auto;
			/deep/ .el-form-item__content {
			}
			.lable {
				padding: 0 10px 0 0;
				color: #fff;
				left: -120px;
				width: 120px;
				font-size: 14px;
				line-height: 34px;
				position: absolute !important;
				text-align: right;
			}
			.el-input {
				width: 100%;
			}
			.el-input /deep/ .el-input__inner {
				border: 0;
				border-radius: 0px;
				padding: 0 10px;
				color: #666;
				width: 100%;
				font-size: 14px;
				height: 34px;
			}
			.el-input /deep/ .el-input__inner:focus {
				border: 0px solid rgba(85, 170, 0, 1.0);
				border-radius: 0;
				padding: 0 10px;
				color: #666;
				width: 100%;
				font-size: 14px;
				height: 34px;
			}
			.el-select {
				width: 100%;
			}
			.el-select /deep/ .el-input__inner {
				border: 0;
				border-radius: 0px;
				padding: 0 10px;
				color: #666;
				width: 100%;
				font-size: 16px;
				height: 34px;
			}
			.el-select /deep/ .el-input__inner:focus {
				border: 0px solid rgba(85, 170, 0, 1.0);
				border-radius: 0;
				padding: 0 10px;
				color: #666;
				width: 100%;
				font-size: 16px;
				height: 34px;
			}
			.el-date-editor {
				width: 100%;
			}
			.el-date-editor /deep/ .el-input__inner {
				border: 0;
				border-radius: 0px;
				padding: 0 10px 0 30px;
				color: #666;
				width: 100%;
				font-size: 16px;
				height: 34px;
			}
			.el-date-editor /deep/ .el-input__inner:focus {
				border: 0px solid rgba(85, 170, 0, 1.0);
				border-radius: 0;
				padding: 0 10px 0 30px;
				color: #666;
				width: 100%;
				font-size: 16px;
				height: 34px;
			}
			.el-date-editor.el-input {
				width: 100%;
			}
			/deep/ .el-upload--picture-card {
				background: transparent;
				border: 0;
				border-radius: 0;
				width: auto;
				height: auto;
				line-height: initial;
				vertical-align: middle;
			}
			/deep/ .upload .upload-img {
				border: 0px dashed rgba(64, 158, 255, 1);
				cursor: pointer;
				border-radius: 0px;
				color: #666;
				background: #fff;
				width: 150px;
				font-size: 32px;
				line-height: 60px;
				text-align: center;
				height: 60px;
			}
			/deep/ .el-upload-list .el-upload-list__item {
				border: 0px dashed rgba(64, 158, 255, 1);
				cursor: pointer;
				border-radius: 0px;
				color: #666;
				background: #fff;
				width: 150px;
				font-size: 32px;
				line-height: 60px;
				text-align: center;
				height: 60px;
			}
			/deep/ .el-upload .el-icon-plus {
				border: 0px dashed rgba(64, 158, 255, 1);
				cursor: pointer;
				border-radius: 0px;
				color: #666;
				background: #fff;
				width: 150px;
				font-size: 32px;
				line-height: 60px;
				text-align: center;
				height: 60px;
			}
			/deep/ .el-upload__tip {
				color: #fff;
				font-size: 15px;
			}
			/deep/ .el-input__inner::placeholder {
				color: #999;
				font-size: 16px;
			}
			.required {
				position: relative;
			}
			.required::after{
				color: red;
				left: 110px;
				position: absolute;
				content: "*";
			}
			.editor {
				background: #fff;
				width: 100%;
				height: auto;
			}
			.editor>.avatar-uploader {
				line-height: 0;
				height: 0;
			}
		}
		.list-item.email {
			input {
				border: 0;
				border-radius: 0px 0 0 0px;
				padding: 0 10px;
				margin: 0;
				color: #666;
				background: #fff;
				flex: 1;
				width: 100%;
				font-size: 14px;
				height: 34px;
			}
			input:focus {
				border: 0px solid rgba(85, 170, 0, 1.0);
				border-radius: 0;
				padding: 0 10px;
				color: #666;
				width: 100%;
				font-size: 14px;
				height: 34px;
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
			button {
				border: 0;
				cursor: pointer;
				border-radius: 0 0px 0px 0;
				padding: 0;
				margin: 3px 0 0;
				color: #fff;
				background: rgba(64, 158, 255, 1);
				width: 150px;
				font-size: 15px;
				height: 34px;
			}
			button:hover {
				opacity: 0.5;
			}
		}
		.register-btn {
			width: 100%;
		}
		.register-btn1 {
			width: 100%;
		}
		.register-btn2 {
			width: 100%;
		}
		.r-btn {
			border: 2px solid rgba(0, 0, 0, 1);
			cursor: pointer;
			border-radius: 8px;
			padding: 0 10px;
			margin: 20px auto 5px;
			color: rgba(0, 0, 0, 1);
			background: #fff;
			display: block;
			width: 80%;
			font-size: 16px;
			height: 34px;
		}
		.r-btn:hover {
			border: 2px solid rgba(85, 170, 0, 1.0);
			color: rgba(85, 170, 0, 1.0);
			opacity: 1;
		}
		.r-login {
			cursor: pointer;
			padding: 0 10%;
			color: #fff;
			display: inline-block;
			text-decoration: underline;
			width: 100%;
			font-size: 14px;
			line-height: 40px;
			text-align: right;
		}
		.r-login:hover {
			opacity: 1;
		}
	}
	.idea-box1 {
		z-index: 1111;
		top: 20px;
		background: url(http://codegen.caihongy.cn/20240712/e60eeb01929043588a299c3af86cdd1b.png) no-repeat;
		width: 124px;
		position: absolute;
		right: -50px;
		height: 167px;
	}
}
	
</style>

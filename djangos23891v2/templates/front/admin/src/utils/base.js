const base = {
    get() {
        return {
            url : "http://localhost:8080/djangos23891v2/",
            name: "djangos23891v2",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于Python的电商用户行为分析系统"
        } 
    }
}
export default base

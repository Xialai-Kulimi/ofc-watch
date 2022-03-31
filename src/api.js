
var jsonify = res => res.json();
function ajax(url){
    return new Promise((resolve, reject) => {
        fetch(`/api/${url}`, {
            credentials: 'include'
        }).then(jsonify).then(resolve).catch(reject)
    })
}


export default {
    getData(url){
        return ajax(url)
    },

}

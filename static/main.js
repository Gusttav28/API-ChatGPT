const divID = document.getElementById('js')



async function get_api() {
    await fetch("http://127.0.0.1:3005/f1")
    if(!res.ok){
        throw new Error("There's some error with the apis");        
    }  
    const response = await res.json()
    console.log("tessst")
    console.log(response)
    return response
} 

get_api()

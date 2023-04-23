let mode_config = localStorage.getItem("dark_mode")

if (mode_config){
    setColorMode(mode_config)
} else {
    localStorage.setItem("dark_mode", "0")
}


let toggle_color_mode_btn = $('.color_mode_toggle')
toggle_color_mode_btn.click(function(event){
    let action_url = event.target.dataset.action_url

    $.ajax({
        method: "GET",
        url: action_url
    })
    .done(function(data){
        localStorage.setItem("dark_mode", "1")

    })


})


function setColorMode(mode){
    // alert('ran')
    
}

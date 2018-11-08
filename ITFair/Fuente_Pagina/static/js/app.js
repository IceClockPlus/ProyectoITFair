$(function(){
    $("#formLogin").validate({
        rules:{
            usuario:{
                required:true
            },
            contrasenia:{
                required:true
            }
        },
        messages:{
            usuario:{
                required:"Campo Obligatorio"
            },
            contrasenia:{
                required:"Campo Obligatorio"
            }
        }
    })

})

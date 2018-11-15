$(document).ready( function() {
    $(document).on('change', '.btn-file :file', function() {
    var input = $(this),
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [label]);
    });

    $('.btn-file :file').on('fileselect', function(event, label) {
        
        var input = $(this).parents('.input-group').find(':text'),
            log = label;
        
        if( input.length ) {
            input.val(log);
        } else {
            if( log ) alert(log);
        }
    
    });
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            
            reader.onload = function (e) {
                $('#img-upload').attr('src', e.target.result);
            }
            
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imgInp").change(function(){
        readURL(this);
    }); 	
});

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

function editar(titulo,resumen,id,icono,video){
    console.log("Editando")
    $("#tituloModal").html("Editando clase: " + titulo)
    $("#titulo").val(titulo)
    $("#resumen").val(resumen)
    $("#id").val(id)
    $("#imagenDeModal").attr("src",icono)
    $("#video").val(video)
}
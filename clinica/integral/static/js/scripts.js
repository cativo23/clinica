$( function() {
    $( "#fechaNac" ).datepicker({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
        onSelect: function(dateText){
        var str = $("#formFecha").serialize();
            $.ajax({
                url: "",
                type: "POST",
                data: 'fechaFiltro='+dateText+'&'+str,
                success: function(data){
                    $("#detallesResultados").html('');
                },
            });
        }
    });
});

$(document).ready(function(){
    $("#nuevoPacienteForm").submit(function(e){
        e.preventDefault();
        $.ajax({
            url: "",
            type: "POST",
            data: $("#nuevoPacienteForm").serialize(),
            success: function(response){
                $("#asigExp").html(response);
            },
            // statusCode:{
            // 400: function(){
            //     var items = [];
            //     $.each(data,function(val){
            //         items.push(val);
            //         });
            //         $("#resultadoPaciente").html(items.join(""));
            //     };
            // }
        });
    });
});

$(document).ready(function(){
    $("#btnObtenerAntecedentes").on('submit',function(e){
        

        alert("KLK");
        $.ajax({
            url: "antecedenteList/14",
            type: "POST",
            data: "",
            success: function(response){
                $("#antecedentes").html(response);
            },
            // statusCode:{
            // 400: function(){
            //     var items = [];
            //     $.each(data,function(val){
            //         items.push(val);
            //         });
            //         $("#resultadoPaciente").html(items.join(""));
            //     };
            // }
        });
    });
});
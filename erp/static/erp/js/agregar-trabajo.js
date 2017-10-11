    update_detalle_guia_despacho = function(){
      i = 1;
      listado = _.reduce(materiales, function(memo, material){
        return memo + "<tr><td>"+(i++)+"</td><td>"+material.nombre+"</td><td>"+material.lote+"</td><td>"+material.cantidad+"</td><td>"+material.unidad+"</td><td><button class='btn btn-danger quitar' data-materialid='"+material.id+"'>Quitar</button></td></tr>";
    }, "");
      $("#detalle_guia_despacho").html(listado);
  };
  




  $("#anadir_material").click(function(e){
      e.preventDefault();
      selected    = $("select[name='material']").find("option:selected");
      bodega = stockBodega(selected);

      material     = {
        id:       $("select[name='unidad']").find("option:selected").val(),
        nombre:   selected.data("nombre"),
        unidad:   $("select[name='unidad']").find("option:selected").html(),
        conversion:   $("select[name='unidad']").find("option:selected").data('conversion'),
        lote:   $("[name='lote']").val(),
        sku:   selected.data("sku"),
        cantidad: parseInt($("input[name='cantidad']").val())
    };

    if(!material.id){
        swal("Selecciona Material", "Selecciona un material para ingresar.", "error");
        return;
    }

    if(isNaN(material.cantidad)){
        swal("Sólo Números", "En cantidad sólo puedes ingresar números.", "error");
        return;
    }

    if((bodega !== undefined && bodega.total*bodega.principal.cantidad < material.cantidad*material.conversion && $("[name='tipo']:checked").val()!="Ingreso") ||
        (bodega == undefined && $("[name='tipo']:checked").val()!="Ingreso")) {
        swal({
            title: "Estas moviendo mas cajas",
            text: "Mueves mas cajas que las disponibles",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Si, deseo hacerlo",
            cancelButtonText: "No, cancelar",
            closeOnConfirm: true,
            closeOnCancel: true
        },
        function(isConfirm){
            if (isConfirm) {
                if(material_ingreado = _.find(materiales, {id: material.id})){
                    material_ingreado.cantidad += material.cantidad
                } else {
                    materiales.push(material);
                }

                update_detalle_guia_despacho();
                $("#form_detalle_material")[0].reset();
                $("[name='material']").find("option[value='']").prop('selected', true).trigger('change');
                $("select").select2();
                return;

            }
        });
} else {
    if(material_ingreado = _.find(materiales, {id: material.id})){
        material_ingreado.cantidad += material.cantidad
    } else {
        materiales.push(material);
    }

    update_detalle_guia_despacho();
    $("#form_detalle_material")[0].reset();
    $("[name='material']").find("option[value='']").prop('selected', true).trigger('change');
    $("select").select2();
}






});
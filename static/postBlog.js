$(document).ready(function(){
    $('#date').datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true,
        todayHighlight: true
    }).on('click', function () {
        $(this).datepicker('show');
    });

    $('#date').datepicker('hide');
});

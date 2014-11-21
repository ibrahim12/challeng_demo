$(document).ready(function(){

    var csrftoken = $('meta[name=csrf-token]').attr('content')

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
        }
    });

    function get_failure_html(result){

        var data = "";
        $.each(result, function(key,value ){
            data += "<li> "+ key + " : " + value + " </li>";
        });

        return "<ul>" + data + "</ul>";

    }

    function show_status(){
        $("#reg-status").removeClass('hide');
        $("#reg-status").slideDown();
    }

    function hide_status(){
        $("#reg-status").slideUp();
    }

    $("#register-form").submit(function(e){

        hide_status();

        var data = $(this).serialize();

        $.ajax({
            url : $REGISTER_URL,
            data : data,
            type : 'POST',
            success :function(result){

                if( parseInt(result.code) == 200){
                      $("#reg-status")
                        .removeClass('alert-danger')
                        .addClass('alert-success')
                        .html(result.data);

                }else{
                      var error_html = get_failure_html(result.data);
                      console.log(error_html);

                      $("#reg-status")
                        .removeClass('alert-success')
                        .addClass('alert-danger')
                        .html(error_html);
                }

                show_status();
            },
            error : function(result){
                $(".reg-status")
                    .removeClass('alert-success')
                    .addClass('alert-danger')
                    .html("Something went wrong.");

                show_status();
            }
        });

        e.preventDefault();


    });



});
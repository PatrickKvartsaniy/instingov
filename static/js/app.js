$(document).ready(function(){

	$('.enable-show-hide').each(function(key,value){
		var field_name = $(this).attr('name');
		switchToggleShowHide(field_name);
	});

	function switchToggleShowHide(input_field){
		if($('#'+input_field+'_field').length){
			initSwitchToggleShowHide(input_field);
			$('input[name="'+input_field+'"]').on('switchChange.bootstrapSwitch', function(event, state) {
				initSwitchToggleShowHide(input_field);
			});
		}
	}

	function switchLanguage(){
		document.cookie = document.cookie + "language=" + this.language
	}

	document.getElementById("lang-ua").onclick = function(){
		
	}
	ua.element.onclick = function(){switchLanguage()}

	const eng = {
		element: document.getElementById("lang-eng"),
		langueage: "eng",
	}
	eng.element.onclick = function(){switchLanguage()}
	

	function initSwitchToggleShowHide(input_field){
		var show_hide_field = input_field+'_field';
		if($('input[name="'+input_field+'"]').is(':checked'))
			$('#'+show_hide_field).show();
		else
			$('#'+show_hide_field).hide();
	}

    $('#user-email-form #template_id').on('change',function(){
      $.ajax({
         url: '/template/content',
         type: "post",
         data: { 'template_id' : $(this).val(),'user_id' : $('#user-email-form').attr('data-extra') },
         error: function(response) {
         },
         success: function(response) {
            if(response.status == 'success'){
              $('#user-email-form #mail_subject').val(response.subject);
              $('#user-email-form #mail_body').summernote('code', response.body);
            }
         },
      });
    });
});
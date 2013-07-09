$('#select_category').change(function () {
	$("select option:selected").each(function () {
		var selected_data = $(this).text();
		alert(selected_data);
		/*
		$.get("http://translate.google.com/translate_tts", function(data){
			
		});
		*/
	});		
});

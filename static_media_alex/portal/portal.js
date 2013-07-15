$('#select_category').change(function () {
	$("select option:selected").each(function () {
		var selected_data = $(this).text().replace(/^\s*|\s*$/g,'');
		var input = selected_data.replace(/ /g, "_");
		
		$.get("/portal/article/"+input+"/author",function(data){
			$("#article_author").html(data);
		});
		
		$.get("/portal/article/"+input,function(data){
			$(".article_justify_text").html(data);
		});
		
	});		
});

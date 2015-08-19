function notification_method(form, method) {
    if (method == "Email") {
      form.find(".email").show();
      form.find(".SMS").hide();
    } else if (method == "SMS") {
      form.find(".email").hide();
      form.find(".SMS").show();
    }
}

$(document).ready(function() {
    $("textarea").height( $("textarea")[0].scrollHeight );
    if ($("form[class=notificationForm]").length > 0) {
      form = $(this);
      method = $("#id_notification_type option:selected").text();
      notification_method(form, method);
      $("#id_notification_type").change(function() {
        method = $(this).find('option:selected').text();
        notification_method(form, method);
      });
    }
});

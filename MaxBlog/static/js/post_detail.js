$('[data-action="like"]').on('click', function() {
  var $btn = $(this);
  $.get($btn.data('url'), function( e ) {
    if (e.status === 'ok')
    {
      if (e.counter > 0)
        $btn.find('span#counter').html(e.counter);
      else
        $btn.find('span#counter').html('');
    } else{
      alert(e)
    }
  });
});

$('[data-action="comment_create"]').on('click', function() {
  var $btn = $(this),
    $form = $($btn.closest('form'));
  $.mainpage($form.attr('action'),
    {
      'csrfmiddlewaretoken': $form.find('input[name="csrfmiddlewaretoken"]').val(),
      'text': $form.find('textarea[name="text"]').val()
    }, function(e) {
      if (e.status === 'ok'){
        $('[data-list="comment"]:last').after(e.comment);
        $form.find('textarea[name="text"]').val('')
      }
      else {
        $form.find('textarea[name="text"]').remove();
        $form.find('tr').remove();
        $btn.before(e.form);
      }
    });
})

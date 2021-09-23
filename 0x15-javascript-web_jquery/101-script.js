/* Task 101 */

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});

$('DIV#remove_item').click(function () {
  $('UL.my_list').remove('<li>Item</li>');
});

$('DIV#clear_list').click(function () {
  $('UL.my_list').empty('<li>Item</li>');
});

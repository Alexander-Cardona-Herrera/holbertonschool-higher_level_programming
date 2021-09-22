/* Task 8 */

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, name) {
    $('UL#list_movies').append('<li>' + name.title + '</li>');
  });
});

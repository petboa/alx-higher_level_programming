#!/usr/bin/node
// script that fetches and prints how to say “Hello” depending of the language
$('document').ready(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $('INPUT#btn_translate').click(function () {
      $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
        $('DIV#hello').html(data.hello);
      });
    });
  });

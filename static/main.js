$(document).ready(function () {
   $('svg#logo').click(function() {
       window.location.href="/";
   })
});

var isNumber = function isNumber(value)
{
   return typeof value === 'number' && isFinite(value);
}

function editQuestion()
{
    if (question_data === undefined || question_data.id === undefined || question_data.title === undefined)
        return;

    let form_type = $('#form-type');
    if (form_type === undefined || form_type.length === 0)
        return;

    let edit_id = $('#edit-id');
    if (edit_id === undefined || edit_id.length === 0)
        return;

    let question_title = $('#question-title');
    if (question_title === undefined || question_title.length === 0)
        return;

    let q_message = $('#q-message');
    if (q_message === undefined || q_message.length === 0)
        return;

    let question_message = $('#question-message');
    if (question_message === undefined || question_message.length === 0)
        return;

    form_type.val('edit');
    edit_id.val(question_data.id);
    question_title.val(question_data.title);
    question_message.val(q_message.html().replaceAll('\n', '').replaceAll('<br>', '\n'));

    question_message.focus();
}

function editAnswer(answer_id) {
    if (answer_id === undefined || !isNumber(answer_id))
        return;

    let a_message = $('#answer-message-' + answer_id.toString());
    if (a_message === undefined || a_message.length === 0)
        return;

    //answer-form-type
    //answer-edit-id
    //answer-message

    let form_type = $('#answer-form-type');
    if (form_type === undefined || form_type.length === 0)
        return;

    let edit_id = $('#answer-edit-id');
    if (edit_id === undefined || edit_id.length === 0)
        return;

    let answer_message = $('#answer-message');
    if (answer_message === undefined || answer_message.length === 0)
        return;

    form_type.val('edit');
    edit_id.val(answer_id);
    answer_message.val(a_message.html().replaceAll('\n', '').replaceAll('<br>', '\n'));
}
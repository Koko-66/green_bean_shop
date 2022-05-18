$(document).ready(function () {
    // Delete product link - formURL is retrieved from the data of the element
    $(".delete").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
    });

    // Add rating form
    $(".add-rating").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url")});
    });

    $(".create-new").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url")});
    });

    $(".edit").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url")});
    });
    
});
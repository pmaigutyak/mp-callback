
CallbackModal = function (url) {

    var $target = $('[data-role=callback]');

    $target.click(function () {

        $.get(url, function (response) {

            var $modal = $(response).modal();

            function toggleSubmitBtn(isActive) {
                $modal.find('[data-role=submit-btn]').prop('disabled', !isActive);
            }

            function handleFormSubmit(event) {

                event.preventDefault();

                toggleSubmitBtn(false);

                $.ajax({
                    method: 'POST',
                    url: url,
                    data: $modal.find('form').serialize(),
                    success: handleFormSubmitSuccess,
                    error: handleFormSubmitError,
                    complete: function () {
                        toggleSubmitBtn(true);
                    }
                });
            }

            function handleSubmitBtnClick() {
                $modal.find('form').submit();
            }

            function handleAnswerTimeChange() {
                var action = $(this).val() === '1' ? 'hide' : 'show';
                $modal.find('[data-role=time-fields]')[action]();
            }

            function removeModal() {
                $modal.remove();
            }

            function handleFormSubmitSuccess(response) {
                $modal.modal('hide');

                if ($.notify) {
                    $.notify({message: response}, {type: 'success'});
                }
            }

            function handleFormSubmitError(response) {
                $modal.find('form').replaceWith(response.responseText);
                refreshTimeFields();
            }

            function refreshTimeFields() {
                $modal.find('input[name=answer_time]:checked').trigger('change');
            }

            $modal.on('submit', 'form', handleFormSubmit);

            $modal.on('click', '[data-role=submit-btn]', handleSubmitBtnClick);

            $modal.on('hidden.bs.modal', removeModal);

            $modal.on('change', '[name=answer_time]', handleAnswerTimeChange);

            refreshTimeFields();
        });

    });

    if ($.fn.tooltip) {
        $target.tooltip();
    }

};

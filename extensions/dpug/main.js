define([
    'require',
    'jquery',
    'base/js/namespace',
    'base/js/events',
    'base/js/utils',
    'base/js/dialog',
    'base/js/i18n',
], function (
    requirejs,
    $,
    Jupyter,
    JupyterEvents,
    utils,
    dialog,
    i18n,
) {
    'use strict';

    function load_ipython_extension() {
        var list_item = $('<li>')
            .attr('id', 'workshop-template')
            .attr('role', 'none')
            .appendTo("#new-menu");

        $('<a>')
            .attr('role', 'menuitem')
            .attr('tabindex', -1)
            .attr('href', '#')
            .text('DPUG Workshop')
            .on('click', function (e) {
                var nb_list = Jupyter.notebook_list;

                var cwd = nb_list.notebook_path || '';
                var dest_name = "Untitled.md"
                var dest_path = utils.url_path_join(cwd, dest_name)
                var api_path = utils.url_path_join("/api", "contents", dest_path)
                console.log(utils)
                
                var w = window.open('', IPython._target);
                utils.ajax({
                        url: "/nbextensions/dpug/template.md",
                        method: "GET",
                        success: function(data) {
                            utils.ajax(api_path, {
                                type: "PUT", 
                                contentType: 'application/json',
                                data: JSON.stringify({
                                    name: dest_name,
                                    path: dest_path,
                                    type: "file",
                                    format: "text",
                                    content: data,
                                })
                            })

                            w.location = utils.url_path_join(
                                nb_list.base_url, 'notebooks', dest_path
                            )
                        },
                        fail: function(e) {
                            w.close();
                            dialog.modal({
                                title: i18n.msg._('Creating File Failed'),
                                body: $('<div/>')
                                    .text(i18n.msg._("An error occurred while creating a new file."))
                                    .append($('<div/>')
                                        .addClass('alert alert-danger')
                                        .text(e.message || e)),
                                buttons: {
                                    OK: {'class': 'btn-primary'}
                                }
                            });
                            console.warn('Error during New file creation', e);
                        }
                });


                nb_list.load_sessions();
                e.preventDefault();

             })
            .appendTo(list_item);

    }

    return {
        load_ipython_extension: load_ipython_extension
    };

});

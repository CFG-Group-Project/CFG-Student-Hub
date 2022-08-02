tinyMCE.init({
    selector: 'textarea#default-editor'
    mode: "textareas",
    theme: "silver",
    plugins: "spellchecker,directionality,paste,searchreplace",
    language: "{{ language }}",
    directionality: "{{ directionality }}",
    spellchecker_languages : "{{ spellchecker_languages }}",
    spellchecker_rpc_url : "{{ spellchecker_rpc_url }}"
});
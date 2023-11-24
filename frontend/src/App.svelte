<script>
    import Router from '/router/Router.svelte';
    import Route from '/router/Route.svelte';
    import Index from "./Index.svelte";
    import Settings from "./Settings.svelte";
    import Results from "./Results.svelte";
    // let response = fetch('http://localhost:8000').then(response => response.json());
</script>

<main>
    <Router>
        <Route path="/" component="{Index}"/>
        <Route path="/settings" component="{Settings}"/>
        <Route path="/results" component="{Results}"/>
    </Router>

    <!--{#await response then text}-->
    <!--    {text["hello"]}-->
    <!--{/await}-->
</main>

<style>

</style>

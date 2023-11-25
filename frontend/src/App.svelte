<script>
    import Router from '/router/Router.svelte';
    import Route from '/router/Route.svelte';
    import Index from "./Index.svelte";
    import Settings from "./Settings.svelte";
    import Results from "./Results.svelte";
    import Predict from "./Predict.svelte";
    // let response = fetch(API_URL).then(response => response.json());
</script>

<main>
    <Router>
        <Route path="/" component="{Index}"/>
        <Route path="/settings" component="{Settings}"/>
        <Route path="/results" component="{Results}"/>
        <Route path="/predict" component="{Predict}"/>
    </Router>

    <!--{#await response then text}-->
    <!--    {text["hello"]}-->
    <!--{/await}-->
</main>

<style>

</style>

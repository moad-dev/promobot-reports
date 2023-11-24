<script>
    let response = fetch('http://localhost:8000').then(response => response.json());
</script>

<main>
    {#await response then text}
        {text["hello"]}
    {/await}
</main>

<style>

</style>

<template>
    <div class="mt-8 px-4 py-4 rounded border border-red-800 mx-24 bg-red-50">
        <h1>Hello World</h1>
        <p class="text-sm">
            {{ message }}
        </p>
    </div>
</template>
<script>
export default {
    name: "HelloWorld",
    data() {
        return {
            message: "Hello Vue!",
        };
    },
};
</script>

<template>
    <div class="icon" :style="'display:'+(icon=='*'?'none':'')">
        <svg v-if="icon!='*'" 
             :class="`icon ${icon}`">
             <use :xlink:href="`#${icon}`">
             </use>
        </svg>
        <svg mlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"
             version="1.1" x="0px" y="0px" aria-hidden="true" style="display:none" viewBox="0 0 40 40"
             preserveAspectRadio="xMidYMin"
        >
            
            <symbol id="icon-person"
                    v-if="icon == '*' || icon === 'icon-person'" 
                    viewBox="0 0 24 24"
            >
                <path d="M12 14.016q2.531 0 5.273 1.102t2.742 2.883v2.016h-16.031v-2.016q0-1.781 2.742-2.883t5.273-1.102zM12 12q-1.641 0-2.813-1.172t-1.172-2.813 1.172-2.836 2.813-1.195 2.813 1.195 1.172 2.836-1.172 2.813-2.813 1.172z"></path>
            </symbol>

            <symbol id="icon-user-add"
                    v-if="icon == '*' || icon === 'icon-user-add'"  
                    viewBox="0 0 20 20">
                <path d="M2 6h-2v2h2v2h2v-2h2v-2h-2v-2h-2v2zM9 6c0-1.657 1.343-3 3-3s3 1.343 3 3v0 2c0 1.657-1.343 3-3 3s-3-1.343-3-3v0-2zM20 15.14c-2.287-1.345-5.038-2.14-7.975-2.14-0.009 0-0.018 0-0.026 0h0.001c-2.91 0-5.65 0.78-8 2.14v2.86h16v-2.86z"></path>
            </symbol>
            
            <symbol id="icon-menu" 
                    v-if="icon == '*' || icon === 'icon-menu'" 
                    viewBox="0 0 20 20"
            >
                <path d="M0 3h20v2h-20v-2zM0 9h20v2h-20v-2zM0 15h20v2h-20v-2z"></path>
            </symbol>
            
            <symbol id="icon-credit" 
                    v-if="icon == '*' || icon === 'icon-credit'" 
                    viewBox="0 0 20 20">
                <path d="M11 16.755v2.245h-2v-2.143c-1.712-0.1-3.066-0.589-4.241-1.797l1.718-1.74c0.859 0.87 2.023 1.16 3.282 1.16 1.565 0 2.405-0.599 2.405-1.702 0-0.483-0.133-0.889-0.42-1.16-0.267-0.251-0.572-0.387-1.202-0.483l-1.642-0.232c-1.164-0.174-2.022-0.541-2.634-1.141-0.648-0.657-0.973-1.546-0.973-2.707 0-2.155 1.382-3.743 3.707-4.1v-1.955h2v1.932c1.382 0.145 2.465 0.62 3.415 1.551l-1.679 1.682c-0.859-0.832-1.889-0.947-2.787-0.947-1.412 0-2.099 0.792-2.099 1.74 0 0.348 0.115 0.716 0.401 0.986 0.267 0.252 0.706 0.464 1.26 0.541l1.602 0.232c1.241 0.174 2.023 0.522 2.596 1.063 0.726 0.696 1.050 1.702 1.050 2.92 0 2.25-1.567 3.662-3.759 4.055z"></path>
            </symbol>
            
        </svg>
    </div>
</template>

<script>
export default {
    name: "icon-shared",
    props: {
        icon: {
            required: true,
            default: "",
            type: String
        }
    }
}
</script>

<style>
    .icon {
        display: inline-block;
        width: 1em;
        height: 1em;
        stroke-width: 0;
        stroke: currentColor;
        fill: currentColor;
    }
</style>
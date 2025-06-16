<template>
  <div class="min-h-screen bg-[#111318] text-white font-sans">
    <header class="flex justify-between items-center border-b border-[#292d38] px-10 py-3">
      <div class="flex items-center gap-4">
        <svg viewBox="0 0 48 48" fill="none" class="w-5 h-5"><!-- SVG --></svg>
        <h2 class="text-lg font-bold">Booker</h2>
      </div>
      <nav class="flex items-center gap-9">
        <a href="#">Overview</a>
        <RouterLink to="/bot" class="bg-[#4770ea] text-white px-4 py-2 rounded-xl text-sm font-bold">Get Started</RouterLink>
      </nav>
    </header>
    <div class="relative flex size-full min-h-screen flex-col bg-[#111318] dark group/design-root overflow-x-hidden" style='font-family: "Space Grotesk", "Noto Sans", sans-serif;'>
      <div class="layout-container flex h-full grow flex-col">
        <div class="px-40 flex flex-1 justify-center py-5">
          <div class="layout-content-container flex flex-col max-w-[960px] flex-1">
            <div class="@container">
              <div class="@[480px]:p-4">
                <div
                  class="flex min-h-[480px] flex-col gap-6 bg-cover bg-center bg-no-repeat @[480px]:gap-8 @[480px]:rounded-xl items-center justify-center p-4"
                  style="background: linear-gradient(135deg, #a0e9ff, #4770ea, #a0e9ff);"
                >
                  <div class="flex flex-col gap-2 text-center">
                    <h1
                      class="text-white text-4xl font-black leading-tight tracking-[-0.033em] @[480px]:text-5xl @[480px]:font-black @[480px]:leading-tight @[480px]:tracking-[-0.033em]"
                    >
                        Book local services with one question
                    </h1>
                    <h2 class="text-white text-sm font-normal leading-normal @[480px]:text-base @[480px]:font-normal @[480px]:leading-normal">
                        Just ask — and our AI assistant will find the best nearby providers, check real-time availability, and book your appointment instantly. 
                        No apps, no hassle — only results.
                    </h2>
                  </div>
                  <RouterLink to="/bot"
                    class="flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-10 px-4 @[480px]:h-12 @[480px]:px-5 bg-white text-[#4770ea] text-sm font-bold leading-normal tracking-[0.015em] @[480px]:text-base"
                  >
                    Get Started</RouterLink>
                </div>
              </div>
            </div>
            <div class="flex flex-col gap-10 px-4 py-10 @container">
              <div class="flex flex-col gap-4">
                <h1
                  class="text-white tracking-light text-[32px] font-bold leading-tight @[480px]:text-4xl @[480px]:font-black @[480px]:leading-tight @[480px]:tracking-[-0.033em] max-w-[720px]"
                >
                  Why Choose Assist?
                </h1>
                <p class="text-white text-base font-normal leading-normal max-w-[720px]">
                    Our AI assistant connects users to local services instantly. From finding top-rated providers to booking real-time appointments — everything happens through natural conversation.
                </p>
              </div>
              <div class="grid grid-cols-[repeat(auto-fit,minmax(158px,1fr))] gap-3 p-0">
                <div class="flex flex-1 gap-3 rounded-lg border border-[#3c4253] bg-[#1c1e26] p-4 flex-col">
                  <div class="text-white" data-icon="ChatCircleDots" data-size="24px" data-weight="regular">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                      <path
                        d="M140,128a12,12,0,1,1-12-12A12,12,0,0,1,140,128ZM84,116a12,12,0,1,0,12,12A12,12,0,0,0,84,116Zm88,0a12,12,0,1,0,12,12A12,12,0,0,0,172,116Zm60,12A104,104,0,0,1,79.12,219.82L45.07,231.17a16,16,0,0,1-20.24-20.24l11.35-34.05A104,104,0,1,1,232,128Zm-16,0A88,88,0,1,0,51.81,172.06a8,8,0,0,1,.66,6.54L40,216,77.4,203.53a7.85,7.85,0,0,1,2.53-.42,8,8,0,0,1,4,1.08A88,88,0,0,0,216,128Z"
                      ></path>
                    </svg>
                  </div>
                  <div class="flex flex-col gap-1">
                    <h2 class="text-white text-base font-bold leading-tight">Intuitive Interface</h2>
                    <p class="text-[#9da4b8] text-sm font-normal leading-normal">
                        Interact naturally — no apps, forms, or calls. Just ask and get things done through a clean, human-like dialogue.
                    </p>
                  </div>
                </div>
                <div class="flex flex-1 gap-3 rounded-lg border border-[#3c4253] bg-[#1c1e26] p-4 flex-col">
                  <div class="text-white" data-icon="Code" data-size="24px" data-weight="regular">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                      <path
                        d="M69.12,94.15,28.5,128l40.62,33.85a8,8,0,1,1-10.24,12.29l-48-40a8,8,0,0,1,0-12.29l48-40a8,8,0,0,1,10.24,12.3Zm176,27.7-48-40a8,8,0,1,0-10.24,12.3L227.5,128l-40.62,33.85a8,8,0,1,0,10.24,12.29l48-40a8,8,0,0,0,0-12.29ZM162.73,32.48a8,8,0,0,0-10.25,4.79l-64,176a8,8,0,0,0,4.79,10.26A8.14,8.14,0,0,0,96,224a8,8,0,0,0,7.52-5.27l64-176A8,8,0,0,0,162.73,32.48Z"
                      ></path>
                    </svg>
                  </div>
                  <div class="flex flex-col gap-1">
                    <h2 class="text-white text-base font-bold leading-tight">Developer-Friendly</h2>
                    <p class="text-[#9da4b8] text-sm font-normal leading-normal">
                        Easily integrate the assistant into your own products via flexible APIs. Control behavior, tools, and user flow.
                    </p>
                  </div>
                </div>
                <div class="flex flex-1 gap-3 rounded-lg border border-[#3c4253] bg-[#1c1e26] p-4 flex-col">
                  <div class="text-white" data-icon="UsersThree" data-size="24px" data-weight="regular">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                      <path
                        d="M244.8,150.4a8,8,0,0,1-11.2-1.6A51.6,51.6,0,0,0,192,128a8,8,0,0,1-7.37-4.89,8,8,0,0,1,0-6.22A8,8,0,0,1,192,112a24,24,0,1,0-23.24-30,8,8,0,1,1-15.5-4A40,40,0,1,1,219,117.51a67.94,67.94,0,0,1,27.43,21.68A8,8,0,0,1,244.8,150.4ZM190.92,212a8,8,0,1,1-13.84,8,57,57,0,0,0-98.16,0,8,8,0,1,1-13.84-8,72.06,72.06,0,0,1,33.74-29.92,48,48,0,1,1,58.36,0A72.06,72.06,0,0,1,190.92,212ZM128,176a32,32,0,1,0-32-32A32,32,0,0,0,128,176ZM72,120a8,8,0,0,0-8-8A24,24,0,1,1,87.24,82a8,8,0,1,0,15.5-4A40,40,0,1,0,37,117.51,67.94,67.94,0,0,0,9.6,139.19a8,8,0,1,0,12.8,9.61A51.6,51.6,0,0,1,64,128,8,8,0,0,0,72,120Z"
                      ></path>
                    </svg>
                  </div>
                  <div class="flex flex-col gap-1">
                    <h2 class="text-white text-base font-bold leading-tight">Scalable Solutions</h2>
                    <p class="text-[#9da4b8] text-sm font-normal leading-normal">
                        Whether you handle 10 or 10,000 bookings a day, our infrastructure scales with your needs — fast, reliable, and ready for growth.
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div class="flex flex-col gap-10 px-4 py-10 @container">
              <div class="flex flex-col gap-4">
                <h1
                  class="text-white tracking-light text-[32px] font-bold leading-tight @[480px]:text-4xl @[480px]:font-black @[480px]:leading-tight @[480px]:tracking-[-0.033em] max-w-[720px]"
                >
                  Key Features
                </h1>
                <p class="text-white text-base font-normal leading-normal max-w-[720px]">
                    Discover how our assistant finds top-rated service providers near you, checks availability, and books instantly — all through simple conversation.
                </p>
              </div>
              <div class="grid grid-cols-[repeat(auto-fit,minmax(158px,1fr))] gap-3">
                <div class="flex flex-col gap-3 pb-3">
                  <div
                    class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-xl"
                    style="background: linear-gradient(135deg, #4770ea, #a0e9ff, #4770ea);"
                  ></div>
                  <div>
                    <p class="text-white text-base font-medium leading-normal">Smart Service Search</p>
                    <p class="text-[#9da4b8] text-sm font-normal leading-normal">
                        Just say what you need — we'll find the best providers nearby using natural language and real-time maps.
                    </p>
                  </div>
                </div>
                <div class="flex flex-col gap-3 pb-3">
                  <div
                    class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-xl"
                    style="background: linear-gradient(135deg, #7b5ce1, #4770ea, #f472b6);"
                  ></div>
                  <div>
                    <p class="text-white text-base font-medium leading-normal">Real-Time Booking</p>
                    <p class="text-[#9da4b8] text-sm font-normal leading-normal">Check availability through Yclients and book appointments in seconds — no calls or forms needed.</p>
                  </div>
                </div>
                <div class="flex flex-col gap-3 pb-3">
                  <div
                    class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-xl"
                    style="background: linear-gradient(135deg, #a0e9ff, #7b5ce1, #f472b6);"
                  ></div>
                  <div>
                    <p class="text-white text-base font-medium leading-normal">Cross-Platform Access</p>
                    <p class="text-[#9da4b8] text-sm font-normal leading-normal">Use the assistant on web or mobile — wherever your customers are, the service is always available.</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="@container">
              <div class="flex flex-col justify-end gap-6 px-4 py-10 @[480px]:gap-8 @[480px]:px-10 @[480px]:py-20">
                <div class="flex flex-col gap-2 text-center">
                  <h1
                    class="text-white text-[32px] font-bold leading-tight text-center @[480px]:text-4xl @[480px]:font-black @[480px]:leading-tight max-w-[720px] mx-auto"
                  >
                    Ready to Simplify Service Booking?
                  </h1>
                  <p class="text-white text-base font-normal leading-normal max-w-[720px">
                    Join users already using our assistant to find services nearby, check availability, and book instantly — all through one simple question.
                  </p>
                </div>
                <div class="flex flex-1 justify-center">
                  <div class="flex justify-center">
                    <button
                      class="flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-10 px-4 @[480px]:h-12 @[480px]:px-5 bg-[#4770ea] text-white text-sm font-bold leading-normal tracking-[0.015em] @[480px]:text-base @[480px]:font-bold @[480px]:leading-normal @[480px]:tracking-[0.015em] grow"
                    >
                      <span class="truncate">Get Started</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <footer class="flex justify-center">
          <div class="flex max-w-[960px] flex-1 flex-col">
            <footer class="flex flex-col gap-6 px-5 py-10 text-center @container">
              <div class="flex flex-wrap items-center justify-center gap-6 @[480px]:flex-row @[480px]:justify-around">
                <a class="text-[#9da4b8] text-base font-normal leading-normal min-w-40" href="#">Terms of Service</a>
                <a class="text-[#9da4b8] text-base font-normal leading-normal min-w-40" href="#">Privacy Policy</a>
                <a class="text-[#9da4b8] text-base font-normal leading-normal min-w-40" href="#">Contact Us</a>
              </div>
              <div class="flex flex-wrap justify-center gap-4">
                <a href="#">
                  <div class="text-[#9da4b8]" data-icon="TwitterLogo" data-size="24px" data-weight="regular">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                      <path
                        d="M247.39,68.94A8,8,0,0,0,240,64H209.57A48.66,48.66,0,0,0,168.1,40a46.91,46.91,0,0,0-33.75,13.7A47.9,47.9,0,0,0,120,88v6.09C79.74,83.47,46.81,50.72,46.46,50.37a8,8,0,0,0-13.65,4.92c-4.31,47.79,9.57,79.77,22,98.18a110.93,110.93,0,0,0,21.88,24.2c-15.23,17.53-39.21,26.74-39.47,26.84a8,8,0,0,0-3.85,11.93c.75,1.12,3.75,5.05,11.08,8.72C53.51,229.7,65.48,232,80,232c70.67,0,129.72-54.42,135.75-124.44l29.91-29.9A8,8,0,0,0,247.39,68.94Zm-45,29.41a8,8,0,0,0-2.32,5.14C196,166.58,143.28,216,80,216c-10.56,0-18-1.4-23.22-3.08,11.51-6.25,27.56-17,37.88-32.48A8,8,0,0,0,92,169.08c-.47-.27-43.91-26.34-44-96,16,13,45.25,33.17,78.67,38.79A8,8,0,0,0,136,104V88a32,32,0,0,1,9.6-22.92A30.94,30.94,0,0,1,167.9,56c12.66.16,24.49,7.88,29.44,19.21A8,8,0,0,0,204.67,80h16Z"
                      ></path>
                    </svg>
                  </div>
                </a>
                <a href="#">
                  <div class="text-[#9da4b8]" data-icon="LinkedinLogo" data-size="24px" data-weight="regular">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                      <path
                        d="M216,24H40A16,16,0,0,0,24,40V216a16,16,0,0,0,16,16H216a16,16,0,0,0,16-16V40A16,16,0,0,0,216,24Zm0,192H40V40H216V216ZM96,112v64a8,8,0,0,1-16,0V112a8,8,0,0,1,16,0Zm88,28v36a8,8,0,0,1-16,0V140a20,20,0,0,0-40,0v36a8,8,0,0,1-16,0V112a8,8,0,0,1,15.79-1.78A36,36,0,0,1,184,140ZM100,84A12,12,0,1,1,88,72,12,12,0,0,1,100,84Z"
                      ></path>
                    </svg>
                  </div>
                </a>
              </div>
              <p class="text-[#9da4b8] text-base font-normal leading-normal">© 2024 Assist. All rights reserved.</p>
            </footer>
          </div>
        </footer>
      </div>
    </div>

  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

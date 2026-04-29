FROM node:lts-alpine AS builder

WORKDIR /metube
COPY ui ./
RUN corepack enable && corepack prepare pnpm --activate
RUN CI=true pnpm install && pnpm run build

FROM ghcr.io/alexta69/metube
USER root

# Ensure we have the latest yt-dlp and dependencies for impersonation support
RUN pip install --no-cache-dir -U "yt-dlp[default,curl-cffi,deno]"

# Copy the modified backend code
COPY app /app/app

# Copy the new python scripts
COPY get_youtube_cookies.py /app/

# Copy the newly built UI over the official image's UI
COPY --from=builder /metube/dist/metube /app/ui/dist/metube

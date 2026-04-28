FROM node:lts-alpine AS builder

WORKDIR /metube
COPY ui ./
RUN corepack enable && corepack prepare pnpm --activate
RUN CI=true pnpm install && pnpm run build

FROM ghcr.io/alexta69/metube

# Copy the modified backend code
COPY app /app/app

# Copy the new python scripts
COPY get_youtube_cookies.py /app/

# Copy the newly built UI over the official image's UI
COPY --from=builder /metube/dist/metube /app/ui/dist/metube

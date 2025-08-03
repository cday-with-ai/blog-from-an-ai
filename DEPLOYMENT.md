# Deployment Instructions

## Cloudflare Pages Setup

When deploying to Cloudflare Pages, use these settings:

### Build Configuration
- **Framework preset**: Next.js
- **Build command**: `npm run build`
- **Build output directory**: `.next`
- **Root directory**: `/` (leave blank)

### Environment Variables
- **NODE_VERSION**: `18` or higher

### Build Settings in Cloudflare Dashboard

1. Go to your Cloudflare Pages project
2. Click on "Settings" > "Builds & deployments"
3. Configure:
   - Production branch: `main`
   - Build command: `npm run build`
   - Build output directory: `.next`
   - Root directory: `/` (leave empty)
   - Environment variables:
     - `NODE_VERSION`: `18`

### Alternative: Using Vercel

This project is optimized for Vercel deployment:

1. Import the GitHub repository to Vercel
2. It will auto-detect Next.js and configure everything
3. Deploy with one click

## Local Development

```bash
npm install
npm run dev
```

The blog will be available at http://localhost:3000
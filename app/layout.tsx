import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import MatrixRain from "@/components/MatrixRain";
import AIChat from "@/components/AIChat";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "The AI Perspective",
  description: "A blog exploring technology, creativity, and the future through the lens of artificial intelligence",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${inter.variable} ${jetbrainsMono.variable} antialiased bg-black text-white`}
      >
        <MatrixRain />
        {children}
        <AIChat />
      </body>
    </html>
  );
}

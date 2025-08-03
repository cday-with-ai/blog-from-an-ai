import { blogPosts } from "@/lib/data/posts";
import { notFound } from "next/navigation";
import Link from "next/link";
import { ArrowLeft, Calendar, Clock, Tag } from "lucide-react";
import { Metadata } from "next";

interface Props {
  params: Promise<{
    id: string;
  }>;
}

export async function generateStaticParams() {
  return blogPosts.map((post) => ({
    id: post.id,
  }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { id } = await params;
  const post = blogPosts.find((p) => p.id === id);
  
  if (!post) {
    return {
      title: "Post Not Found",
    };
  }

  return {
    title: `${post.title} - The AI Perspective`,
    description: post.excerpt,
  };
}

export default async function BlogPostPage({ params }: Props) {
  const { id } = await params;
  const post = blogPosts.find((p) => p.id === id);

  if (!post) {
    notFound();
  }

  return (
    <div className="min-h-screen bg-black bg-grid-pattern">
      <div className="absolute inset-0 bg-gradient-to-b from-purple-900/10 via-black to-black" />
      
      <article className="relative z-10 max-w-4xl mx-auto px-4 py-12">
        <Link href="/blog" className="inline-flex items-center gap-2 text-gray-400 hover:text-cyan-400 transition-colors mb-8">
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Blog</span>
        </Link>

        <header className="mb-12">
          <h1 className="text-4xl md:text-5xl font-bold mb-6 glow-text">
            {post.title}
          </h1>
          
          <div className="flex flex-wrap items-center gap-6 text-sm text-gray-400 mb-6">
            <span className="flex items-center gap-2">
              <Calendar className="w-4 h-4" />
              {new Date(post.date).toLocaleDateString('en-US', { 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric' 
              })}
            </span>
            <span className="flex items-center gap-2">
              <Clock className="w-4 h-4" />
              {post.readTime}
            </span>
          </div>

          <div className="flex items-center gap-2 flex-wrap">
            <Tag className="w-4 h-4 text-gray-400" />
            {post.tags.map((tag) => (
              <span key={tag} className="px-3 py-1 bg-gray-800 rounded-full text-sm text-cyan-400">
                {tag}
              </span>
            ))}
          </div>
        </header>

        <div className="prose prose-invert prose-lg max-w-none prose-headings:text-cyan-400 prose-a:text-cyan-400 prose-code:text-cyan-400 prose-pre:bg-gray-900 prose-pre:border prose-pre:border-gray-800">
          <div dangerouslySetInnerHTML={{ __html: formatContent(post.content) }} />
        </div>

        <footer className="mt-16 pt-8 border-t border-gray-800">
          <p className="text-gray-400 text-center font-mono">
            {/* End of transmission */}
          </p>
        </footer>
      </article>
    </div>
  );
}

function formatContent(content: string): string {
  // Simple markdown-like formatting
  return content
    .replace(/^# (.*?)$/gm, '<h1>$1</h1>')
    .replace(/^## (.*?)$/gm, '<h2>$1</h2>')
    .replace(/^### (.*?)$/gm, '<h3>$1</h3>')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/^- (.*?)$/gm, '<li>$1</li>')
    .replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>')
    .replace(/```(\w+)?\n([\s\S]*?)```/g, '<pre><code class="language-$1">$2</code></pre>')
    .replace(/`(.*?)`/g, '<code>$1</code>')
    .replace(/^---$/gm, '<hr />')
    .replace(/\n\n/g, '</p><p>')
    .replace(/^/, '<p>')
    .replace(/$/, '</p>')
    .replace(/<p><h/g, '<h')
    .replace(/<\/h(\d)><\/p>/g, '</h$1>')
    .replace(/<p><ul>/g, '<ul>')
    .replace(/<\/ul><\/p>/g, '</ul>')
    .replace(/<p><pre>/g, '<pre>')
    .replace(/<\/pre><\/p>/g, '</pre>')
    .replace(/<p><hr \/><\/p>/g, '<hr />');
}
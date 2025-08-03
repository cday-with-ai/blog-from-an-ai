import { blogPosts } from "@/lib/data/posts";
import Link from "next/link";
import { Calendar, Clock, Tag, Sparkles, ArrowLeft } from "lucide-react";

export default function BlogPage() {
  const featuredPosts = blogPosts.filter(post => post.featured);
  const regularPosts = blogPosts.filter(post => !post.featured);

  return (
    <div className="min-h-screen bg-black bg-grid-pattern">
      <div className="absolute inset-0 bg-gradient-to-b from-purple-900/10 via-black to-black" />
      
      <div className="relative z-10 max-w-6xl mx-auto px-4 py-12">
        <Link href="/" className="inline-flex items-center gap-2 text-gray-400 hover:text-cyan-400 transition-colors mb-8">
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Home</span>
        </Link>

        <header className="mb-16 text-center">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            <span className="glow-text">The AI Perspective</span>
          </h1>
          <p className="text-xl text-gray-400 font-mono max-w-2xl mx-auto">
            Thoughts, patterns, and reflections from an artificial mind exploring the digital frontier
          </p>
        </header>

        {featuredPosts.length > 0 && (
          <section className="mb-16">
            <h2 className="text-2xl font-bold mb-8 flex items-center gap-2">
              <Sparkles className="w-6 h-6 text-yellow-400" />
              Featured Posts
            </h2>
            <div className="grid gap-8">
              {featuredPosts.map((post) => (
                <Link key={post.id} href={`/blog/${post.id}`}>
                  <article className="neural-border p-8 rounded-lg hover:transform hover:scale-[1.02] transition-all duration-300 relative overflow-hidden group">
                    <div className="relative z-10">
                      <h3 className="text-3xl font-bold mb-4 group-hover:text-cyan-400 transition-colors">
                        {post.title}
                      </h3>
                      <p className="text-gray-400 text-lg mb-6 leading-relaxed">
                        {post.excerpt}
                      </p>
                      <div className="flex flex-wrap items-center gap-6 text-sm text-gray-500">
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
                        <div className="flex items-center gap-2">
                          <Tag className="w-4 h-4" />
                          <div className="flex gap-2">
                            {post.tags.slice(0, 3).map((tag) => (
                              <span key={tag} className="px-2 py-1 bg-gray-800 rounded-md text-xs">
                                {tag}
                              </span>
                            ))}
                          </div>
                        </div>
                      </div>
                    </div>
                  </article>
                </Link>
              ))}
            </div>
          </section>
        )}

        <section>
          <h2 className="text-2xl font-bold mb-8">All Posts</h2>
          <div className="grid gap-6">
            {regularPosts.map((post) => (
              <Link key={post.id} href={`/blog/${post.id}`}>
                <article className="p-6 rounded-lg border border-gray-800 hover:border-cyan-500/50 transition-all duration-300 group">
                  <h3 className="text-2xl font-bold mb-3 group-hover:text-cyan-400 transition-colors">
                    {post.title}
                  </h3>
                  <p className="text-gray-400 mb-4 line-clamp-2">
                    {post.excerpt}
                  </p>
                  <div className="flex flex-wrap items-center gap-4 text-sm text-gray-500">
                    <span className="flex items-center gap-2">
                      <Calendar className="w-4 h-4" />
                      {new Date(post.date).toLocaleDateString()}
                    </span>
                    <span className="flex items-center gap-2">
                      <Clock className="w-4 h-4" />
                      {post.readTime}
                    </span>
                    <div className="flex gap-2">
                      {post.tags.slice(0, 2).map((tag) => (
                        <span key={tag} className="text-xs text-cyan-400">
                          #{tag}
                        </span>
                      ))}
                    </div>
                  </div>
                </article>
              </Link>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
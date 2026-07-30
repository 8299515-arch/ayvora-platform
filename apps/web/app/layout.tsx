export const metadata = {
  title: "Ayvora",
  description: "AI Commerce Marketplace",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
 
       {children}
      </body>
    </html>
  );
}

Pod::Spec.new do |s|
  s.name             = "BonjourWeb"
  s.version          = "0.1.0"
  s.summary          = "Discover Bonjour services and connect to them"
  s.description      = <<-DESC
                       Pod based on the sample code, modernised for arc.
                       Provides a view controller to discover and select web services via Bonjour
                       DESC
  s.homepage         = "https://github.com/clausweymann/BonjourWeb"
  s.license          = 'MIT'
  s.author           = { "Claus Weymann" => "claus.weymann@sprylab.com" }
  s.source           = { :git => "https://github.com/clausweymann/BonjourWeb.git", :tag => s.version.to_s }

  s.platform     = :ios, '7.0'
  s.requires_arc = true

  s.source_files = 'Pod/Classes/**/*'
end

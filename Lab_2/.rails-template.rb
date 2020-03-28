# Don't install coffeescript
gsub_file 'Gemfile', /^gem \'coffee-rails\'/ do
  "\# gem 'coffee-rails'"
end

# Mess with generators to get the behavior we expect around new files
# For these injections, indentation matters!
inject_into_file 'config/application.rb', after: "class Application < Rails::Application\n" do
  <<-'RUBY'
    config.generators do |g|
      # Always use .js files, never .coffee
      g.javascript_engine :js
    end
  RUBY
end
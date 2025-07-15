# Simple To-Do List App in Ruby

tasks = []

# Function to display the main menu
def show_menu
  puts "\n== TO-DO LIST MENU =="
  puts "1. Show all tasks"
  puts "2. Add a new task"
  puts "3. Mark a task as done"
  puts "4. Delete a task"
  puts "5. Edit a task name"
  puts "6. Clear all completed tasks"
  puts "7. Show only completed or pending tasks"
  puts "8. Exit"
  print "\nEnter your choice (1-8): "
end

# Function to display all tasks
def list_tasks(task_list)
  if task_list.empty?
    puts "No tasks available."
  else
    puts "\nTask List:"
    task_list.each_with_index do |task, index|
      status = task[:done] ? "[Done]" : "[Pending]"
      puts "#{index + 1}. #{status} #{task[:name]}"
    end
  end
end

# Main program loop
loop do
  show_menu
  choice = gets.chomp

  case choice
  when "1"
    list_tasks(tasks)

  when "2"
    print "Enter task name: "
    name = gets.chomp.strip
    if name.empty?
      puts "Task name cannot be empty."
    else
      tasks << { name: name, done: false }
      puts "Task added successfully."
    end

  when "3"
    list_tasks(tasks)
    print "Enter the task number to mark as done: "
    index = gets.chomp.to_i - 1
    if tasks[index]
      tasks[index][:done] = true
      puts "Task marked as done."
    else
      puts "Invalid task number."
    end

  when "4"
    list_tasks(tasks)
    print "Enter the task number to delete: "
    index = gets.chomp.to_i - 1
    if tasks[index]
      removed = tasks.delete_at(index)
      puts "Task deleted: #{removed[:name]}"
    else
      puts "Invalid task number."
    end

  when "5"
    list_tasks(tasks)
    print "Enter the task number to edit: "
    index = gets.chomp.to_i - 1
    if tasks[index]
      print "Enter new name for the task: "
      new_name = gets.chomp.strip
      if new_name.empty?
        puts "Task name cannot be empty."
      else
        tasks[index][:name] = new_name
        puts "Task updated successfully."
      end
    else
      puts "Invalid task number."
    end

  when "6"
    initial_size = tasks.size
    tasks.reject! { |task| task[:done] }
    removed_count = initial_size - tasks.size
    if removed_count > 0
      puts "#{removed_count} completed task(s) removed."
    else
      puts "No completed tasks to remove."
    end

  when "7"
    print "Show (1) Completed or (2) Pending tasks? "
    option = gets.chomp
    filtered = if option == "1"
                 tasks.select { |t| t[:done] }
               elsif option == "2"
                 tasks.reject { |t| t[:done] }
               else
                 puts "Invalid option."
                 []
               end
    list_tasks(filtered)

  when "8"
    puts "Exiting program."
    break

  else
    puts "Invalid choice. Please enter a number between 1 and 8."
  end
end
